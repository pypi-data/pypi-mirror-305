#!/opt/homebrew/anaconda3/envs/quantfin/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/26 上午10:34
# @Author  : @Zhenxi Zhang
# @File    : __init__.py.py
# @Software: PyCharm

import os
import sys
import site
from typing import NoReturn


def mac_env_init_windpy() -> NoReturn:
    """
    初始化 WindPy 环境配置。

    此函数执行以下操作：
    1. 确保用户的站点包目录存在。
    2. 在站点包目录中创建 WindPy.py 的符号链接。
    3. 创建指向 Wind 数据目录的符号链接。

    Raises:
        FileExistsError: 如果目标文件已存在且不是符号链接，则抛出此异常。
        FileNotFoundError: 如果源文件或目录不存在，则抛出此异常。
    """
    # 获取Python版本号
    _version_py = sys.version.split(" ")[0]

    if _version_py.startswith("3.12"):
        # 对于Python 3.12及更高版本，使用系统命令创建符号链接
        # 注意：这里使用os.system执行shell命令来创建符号链接
        import distutils.sysconfig

        os.system(
            'ln -sf "/Applications/Wind API.app/Contents/python/WindPy.py"'
            + " "
            + distutils.sysconfig.get_python_lib(prefix=sys.prefix)
        )
        os.system("ln -sf ~/Library/Containers/com.wind.mac.api/Data/.Wind ~/.Wind")

    else:
        # 获取用户站点包目录
        user_site_packages = site.getusersitepackages()

        # 创建用户站点包目录，如果不存在的话
        os.makedirs(user_site_packages, exist_ok=True)

        # 创建 WindPy.py 的符号链接
        # 指定 WindPy.py 源文件的位置
        windpy_src = "/Applications/Wind API.app/Contents/python/WindPy.py"

        # 构建符号链接的目标位置
        windpy_dest = os.path.join(user_site_packages, "WindPy.py")

        # 创建符号链接
        os.symlink(windpy_src, windpy_dest)

        # 创建 ~/.Wind 的符号链接指向 ~/Library/Containers/com.wind.mac.api/Data/.Wind
        # 扩展用户目录变量
        wind_data_src = "~/Library/Containers/com.wind.mac.api/Data/.Wind"

        # 构建符号链接的目标位置
        wind_data_dest = os.path.expanduser("~/.Wind")

        # 创建符号链接
        os.symlink(wind_data_src, wind_data_dest)


class FrozenHashError(TypeError):
    """自定义异常类，用于处理在计算哈希值时发生的错误。"""

    pass


class FrozenDict(dict):
    """
    一个不可变的字典子类，可以哈希并且可以用作其他字典的键或集合中的元素。
    FrozenDict 类似于 frozenset 之于 set，它是 dict 的不可变版本。

    特性：
    - 不可变性：一旦创建就不能修改。
    - 哈希性：可以作为其他字典的键或集合中的元素。

    注意：
    - 尝试修改 FrozenDict 实例将引发 TypeError。
    - 内部使用了 __slots__ 来节省内存。
    """

    __slots__ = ("_hash",)

    def updated(self, *args, **kwargs) -> "FrozenDict":
        """
        创建一个新的 FrozenDict 实例，并添加或更新键值对。

        参数:
            *args: 可迭代对象，包含键值对。
            **kwargs: 关键字参数，用于添加或更新键值对。

        返回:
            FrozenDict: 新的 FrozenDict 实例。
        """
        new_dict = dict(self)
        new_dict.update(*args, **kwargs)
        return type(self)(new_dict)

    @classmethod
    def fromkeys(cls, keys, value=None) -> "FrozenDict":
        """
        创建一个新的 FrozenDict 实例，其中所有的键都映射到相同的值。

        参数:
            keys: 可迭代的对象，包含要创建的键。
            value: 单一的值，所有键都映射到此值。

        返回:
            FrozenDict: 新的 FrozenDict 实例。
        """
        return cls(dict.fromkeys(keys, value))

    def __repr__(self) -> str:
        """
        返回 FrozenDict 的字符串表示形式。

        返回:
            str: 字典的字符串表示形式，包括类名。
        """
        class_name = self.__class__.__name__
        return f"{class_name}({dict.__repr__(self)})"

    def __reduce_ex__(self, protocol) -> tuple:
        """
        用于支持 pickle 协议的序列化方法。

        参数:
            protocol: 序列化协议的版本号。

        返回:
            tuple: 包含类本身和构造函数所需参数的元组。
        """
        return type(self), (dict(self),)

    def __hash__(self) -> int:
        """
        计算 FrozenDict 的哈希值。

        返回:
            int: FrozenDict 的哈希值。
        """
        try:
            ret = self._hash
        except AttributeError:
            try:
                ret = self._hash = hash(frozenset(self.items()))
            except Exception as e:
                ret = self._hash = FrozenHashError(e)

        if isinstance(ret, FrozenHashError):
            raise ret

        return ret

    def __copy__(self) -> "FrozenDict":
        """
        返回自身，因为 FrozenDict 是不可变的。

        返回:
            FrozenDict: 当前实例。
        """
        return self  # 不可变类型不需要复制，参考 tuple 的行为

    # 下面的方法都会引发 TypeError，因为 FrozenDict 是不可变的

    def _raise_frozen_typeerror(self, *a, **kw):
        """raises a TypeError, because FrozenDicts are immutable"""
        raise TypeError("%s object is immutable" % self.__class__.__name__)

    __ior__ = __setitem__ = __delitem__ = update = setdefault = pop = popitem = (
        clear
    ) = _raise_frozen_typeerror
    del _raise_frozen_typeerror
