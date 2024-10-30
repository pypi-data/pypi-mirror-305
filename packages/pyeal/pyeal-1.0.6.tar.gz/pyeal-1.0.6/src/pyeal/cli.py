# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/8 12:02
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function, division

if False:
    from typing import *

import datetime
import json
import locale
import os.path
import sys
import uuid
from collections import OrderedDict

import argparse

from pyeal.res import LocalRes, DirectoryRes, MergeRes
from pyeal.seal import seal
from pyeal.exc import *
from pyeal._command import call_command

PATH = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    def __init__(self, root, config_file='pyeal.json'):
        root = os.path.abspath(root)
        self.root_path = os.path.abspath(root)
        self.config_file = config_file
        self.src_path = os.sep.join((self.root_path, 'src'))
        self.lib_path = os.sep.join((self.root_path, 'lib'))
        self.build_path = os.sep.join((self.root_path, 'build'))
        self.middle_path = os.sep.join((root, 'build', 'middle'))
        self.out_path = os.sep.join((root, 'build', 'out'))

        self.root = LocalRes(self.root_path)
        self.src = LocalRes(self.src_path)
        self.lib = LocalRes(self.lib_path)
        self.build = LocalRes(self.build_path)
        self.middle = LocalRes(self.middle_path)
        self.out = LocalRes(self.out_path)

    def get_root_res(self):
        return LocalRes(self.root_path)

    def get_source_res(self):
        outer_lib_path_list = self.get('outer_lib', [])
        lib_paths = self.get('lib', ['lib'] + outer_lib_path_list)
        src_paths = self.get('src', ['src'] + lib_paths)
        src_res_list = [LocalRes(i) for i in src_paths]
        return MergeRes(*src_res_list)

    def get_config(self):
        return json.loads(self.root.read_string(self.config_file))

    @property
    def config_data(self):
        return self.get_config()

    @property
    def type(self):
        return self.config_data["type"]

    @property
    def name(self):
        return self.config_data["name"]

    def get_script(self):
        script = self.config_data.get("exec_script", None)
        if script is None:
            index_module = self.config_data.get("index_module", "index.py")
            script = self.root.read(index_module)
        return script

    def get_icon(self):
        return self.root.read('icon.ico')

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def ass(self, key):
        c = self.get(key, None)
        if c is None:
            raise ConfigException("需要名为<{}>的配置项".format(key))
        return c


def target_is_exec(config):
    """
    :type config: Config
    """
    seal(
        config.get_source_res(),
        config.out,
        config.name,
        config.get_script(),
        config.get('imp_name', config.name),
    )


def target_is_maya_plugin(config):
    """
    :type config: Config
    """
    m0 = DirectoryRes(config.middle, "m0")

    seal(
        config.get_source_res(),
        m0,
        config.name,
        config.get_script(),
        config.get('imp_name', config.name)
    )
    plugin_path = "dist/plugin"
    for f in m0.files():
        config.out.write('/'.join((plugin_path, f)), m0.read(f))
    with open(os.sep.join((PATH, 'assets', "mel_template_lib.mel")), "rb") as f:
        mel_template_lib_code = f.read().decode("utf-8")
    mel_template = r'''
startInstall(
"exec(compile(open(plugin_path+" + <<exec_file_name>> + ",'rb').read(), plugin_path+" + <<exec_file_name>> + ", 'exec'), globals(), locals())", 
<<ann>>, 
"dist/log.ico", 
<<plugin_path>>
);
'''

    mel_template = mel_template.replace(
        '<<exec_file_name>>',
        '"\'{}.py\'"'.format(config.name)
    )
    mel_template = mel_template.replace(
        '<<ann>>',
        '"{}"'.format(config.get('annotation', '这个插件作者很懒没有写注释哦~'))
    )
    mel_template = mel_template.replace(
        '<<plugin_path>>',
        '"{}/"'.format(plugin_path)
    )
    # 以系统编码写入安装文件
    config.out.write('install.mel', (mel_template_lib_code + mel_template).encode(locale.getpreferredencoding()))
    config.out.write('/'.join(('dist', 'log.ico')), config.get_icon())


def target_is_template(config):
    """
    :type config: Config
    """
    template = DirectoryRes(config.root, 'template')
    template_output = DirectoryRes(config.out, config.ass('template-output'))

    for f in template.files():
        config.out.write(f, template.read(f))

    seal(
        config.get_source_res(),
        template_output,
        config.name,
        config.get_script(),
        config.get('imp_name', config.name),
    )


target_types = {
    'package': target_is_exec,
    'maya-plugin': target_is_maya_plugin,
    'template': target_is_template,
}  # type: Dict[AnyStr, Callable[[Config], None]]


def _call_command_list(command_list, build_data):
    for i in command_list:
        if isinstance(i, list):
            call_command(i, build_data)
        elif isinstance(i, dict):
            try:
                is_do_command = eval(i.get('if_expression', 'True'), dict(), build_data)
            except:
                is_do_command = False
            if is_do_command:
                command = i.get('true_command', None)
                if command:
                    call_command(command, build_data)
            else:
                command = i.get('false_command', None)
                if command:
                    call_command(command, build_data)
        else:
            raise SealException("未知的命令格式")


config_templates = {
    "package": OrderedDict([
        ("type", "package"),
        ("exec_script", ""),
    ]),
    "maya-plugin": OrderedDict([
        ("type", "maya-plugin"),
        ("exec_script", ""),
    ]),
    "template": OrderedDict([
        ("type", "template"),
        ("exec_script", ""),
        ("template-output", "src"),
    ]),
}


class SubCommand(object):
    name = None
    help = ''

    def __init__(self, parser):
        # type: (argparse.ArgumentParser) -> None
        self.parser = parser
        self.parser.set_defaults(func=self.process)
        self.init_parser()

    def init_parser(self):
        raise NotImplementedError()

    def process(self, args):
        raise NotImplementedError()


class BuildCommand(SubCommand):
    name = 'build'
    help = 'build project'

    def init_parser(self):
        # 获得所有位置参数，传递给build data。
        self.parser.add_argument('args', nargs='*', help='args')
        # config
        self.parser.add_argument('-cf', '--config_file', type=str, default='pyeal.json', help='config file')

    def process(self, args):
        config = Config(os.path.abspath("."), args.config_file)
        config.build.clean()
        command_list_at_start = config.get('command_list_at_start', [])
        command_list_at_end = config.get('command_list_at_end', [])
        build_data = {
            'build_uuid': uuid.uuid4().hex,
            'build_time': datetime.datetime.now(),
            'src_path': config.src_path,
            'lib_path': config.lib_path,
            'build_path': config.build_path,
            'middle_path': config.middle_path,
            'out_path': config.out_path,
            'args': args.args,
            'name': config.name,
        }

        _call_command_list(command_list_at_start, build_data)

        target_type_func = target_types.get(config.type)

        if target_type_func is None:
            raise SealException("未知编译类型")

        target_type_func(config)

        _call_command_list(command_list_at_end, build_data)


class InitCommand(SubCommand):
    name = 'init'
    help = 'init project, you can use -t to choose a template'

    def init_parser(self):
        self.parser.add_argument('-t', '--template',
                                 choices=config_templates.keys(),
                                 type=str,
                                 default='package',
                                 help='choose a template'
                                 )
        self.parser.add_argument('-n', '--name', type=str, default='your_name', help='package name')
        self.parser.add_argument('-cf', '--config_file', type=str, default='pyeal.json',
                                 help='config file')

    def process(self, args):
        root_path = os.path.abspath(".")
        root = LocalRes(root_path)

        template = config_templates[args.template]
        template['name'] = args.name

        root.write_string(
            args.config_file,
            json.dumps(template, indent=2, ensure_ascii=False)
        )

        src = os.sep.join((root_path, "src"))
        if not os.path.isdir(src):
            os.makedirs(src)
        build = os.sep.join((root_path, "build"))
        if not os.path.isdir(build):
            os.makedirs(build)

        if args.template == 'maya-plugin':
            with open(os.sep.join((PATH, 'assets', "icon.ico")), "rb") as f:
                root.write("icon.ico", f.read())


class CleanCommand(SubCommand):
    name = 'clean'
    help = 'clean project'

    def init_parser(self):
        self.parser.add_argument('-cf', '--config_file', type=str, default='pyeal.json', help='config file')

    def process(self, args):
        config = Config(os.path.abspath("."), args.config_file)
        config.build.clean()


commands = [
    BuildCommand,
    InitCommand,
    CleanCommand,
]  # type: List[SubCommand]


def main(argv):
    root = os.path.abspath(".")

    parser = argparse.ArgumentParser(
        description='Python 打包编译工具',
        prog='pyeal',
    )
    subparsers = parser.add_subparsers(
        title='subcommands',
        description='valid subcommands',
        help='sub-command help',
    )
    for sub_command in commands:
        sub_command(subparsers.add_parser(sub_command.name, help=sub_command.help))

    args = parser.parse_args(argv)
    args.func(args)
