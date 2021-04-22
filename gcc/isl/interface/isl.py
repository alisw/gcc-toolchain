isl_dlname='libisl.so.21'
import os
from ctypes import *
from ctypes.util import find_library

isl_dyld_library_path = os.environ.get('ISL_DYLD_LIBRARY_PATH')
if isl_dyld_library_path != None:
    os.environ['DYLD_LIBRARY_PATH'] =  isl_dyld_library_path
try:
    isl = cdll.LoadLibrary(isl_dlname)
except:
    isl = cdll.LoadLibrary(find_library("isl"))
libc = cdll.LoadLibrary(find_library("c"))

class Error(Exception):
    pass

class Context:
    defaultInstance = None

    def __init__(self):
        ptr = isl.isl_ctx_alloc()
        self.ptr = ptr

    def __del__(self):
        isl.isl_ctx_free(self)

    def from_param(self):
        return c_void_p(self.ptr)

    @staticmethod
    def getDefaultInstance():
        if Context.defaultInstance == None:
            Context.defaultInstance = Context()
        return Context.defaultInstance

isl.isl_ctx_alloc.restype = c_void_p
isl.isl_ctx_free.argtypes = [Context]

class union_pw_multi_aff(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is pw_multi_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_multi_aff_from_pw_multi_aff(isl.isl_pw_multi_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_multi_aff_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        if len(args) == 1 and args[0].__class__ is union_pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_multi_aff_from_union_pw_aff(isl.isl_union_pw_aff_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_pw_multi_aff_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is union_pw_multi_aff:
                arg0 = union_pw_multi_aff(arg0)
        except:
            raise
        ptr = isl.isl_union_pw_multi_aff_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_pw_multi_aff("""%s""")' % s
        else:
            return 'isl.union_pw_multi_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_multi_aff:
                arg0 = union_pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_multi_aff:
                arg1 = union_pw_multi_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_pw_multi_aff_add(isl.isl_union_pw_multi_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
        obj = union_pw_multi_aff(ctx=ctx, ptr=res)
        return obj
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_multi_aff:
                arg0 = union_pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_multi_aff:
                arg1 = union_pw_multi_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_pw_multi_aff_flat_range_product(isl.isl_union_pw_multi_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
        obj = union_pw_multi_aff(ctx=ctx, ptr=res)
        return obj
    def pullback(arg0, arg1):
        if arg1.__class__ is union_pw_multi_aff:
            res = isl.isl_union_pw_multi_aff_pullback_union_pw_multi_aff(isl.isl_union_pw_multi_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = union_pw_multi_aff(ctx=ctx, ptr=res)
            return obj
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_multi_aff:
                arg0 = union_pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_multi_aff:
                arg1 = union_pw_multi_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_pw_multi_aff_union_add(isl.isl_union_pw_multi_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
        obj = union_pw_multi_aff(ctx=ctx, ptr=res)
        return obj

isl.isl_union_pw_multi_aff_from_pw_multi_aff.restype = c_void_p
isl.isl_union_pw_multi_aff_from_pw_multi_aff.argtypes = [c_void_p]
isl.isl_union_pw_multi_aff_read_from_str.restype = c_void_p
isl.isl_union_pw_multi_aff_read_from_str.argtypes = [Context, c_char_p]
isl.isl_union_pw_multi_aff_from_union_pw_aff.restype = c_void_p
isl.isl_union_pw_multi_aff_from_union_pw_aff.argtypes = [c_void_p]
isl.isl_union_pw_multi_aff_add.restype = c_void_p
isl.isl_union_pw_multi_aff_add.argtypes = [c_void_p, c_void_p]
isl.isl_union_pw_multi_aff_flat_range_product.restype = c_void_p
isl.isl_union_pw_multi_aff_flat_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_union_pw_multi_aff_pullback_union_pw_multi_aff.restype = c_void_p
isl.isl_union_pw_multi_aff_pullback_union_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_union_pw_multi_aff_union_add.restype = c_void_p
isl.isl_union_pw_multi_aff_union_add.argtypes = [c_void_p, c_void_p]
isl.isl_union_pw_multi_aff_copy.restype = c_void_p
isl.isl_union_pw_multi_aff_copy.argtypes = [c_void_p]
isl.isl_union_pw_multi_aff_free.restype = c_void_p
isl.isl_union_pw_multi_aff_free.argtypes = [c_void_p]
isl.isl_union_pw_multi_aff_to_str.restype = POINTER(c_char)
isl.isl_union_pw_multi_aff_to_str.argtypes = [c_void_p]

class multi_union_pw_aff(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is union_pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_union_pw_aff_from_union_pw_aff(isl.isl_union_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is multi_pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_union_pw_aff_from_multi_pw_aff(isl.isl_multi_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_union_pw_aff_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_multi_union_pw_aff_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is multi_union_pw_aff:
                arg0 = multi_union_pw_aff(arg0)
        except:
            raise
        ptr = isl.isl_multi_union_pw_aff_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.multi_union_pw_aff("""%s""")' % s
        else:
            return 'isl.multi_union_pw_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_union_pw_aff:
                arg0 = multi_union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_union_pw_aff_add(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        obj = multi_union_pw_aff(ctx=ctx, ptr=res)
        return obj
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_union_pw_aff:
                arg0 = multi_union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_union_pw_aff_flat_range_product(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        obj = multi_union_pw_aff(ctx=ctx, ptr=res)
        return obj
    def pullback(arg0, arg1):
        if arg1.__class__ is union_pw_multi_aff:
            res = isl.isl_multi_union_pw_aff_pullback_union_pw_multi_aff(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = multi_union_pw_aff(ctx=ctx, ptr=res)
            return obj
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_union_pw_aff:
                arg0 = multi_union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_union_pw_aff_range_product(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        obj = multi_union_pw_aff(ctx=ctx, ptr=res)
        return obj
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_union_pw_aff:
                arg0 = multi_union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_union_pw_aff_union_add(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        obj = multi_union_pw_aff(ctx=ctx, ptr=res)
        return obj

isl.isl_multi_union_pw_aff_from_union_pw_aff.restype = c_void_p
isl.isl_multi_union_pw_aff_from_union_pw_aff.argtypes = [c_void_p]
isl.isl_multi_union_pw_aff_from_multi_pw_aff.restype = c_void_p
isl.isl_multi_union_pw_aff_from_multi_pw_aff.argtypes = [c_void_p]
isl.isl_multi_union_pw_aff_read_from_str.restype = c_void_p
isl.isl_multi_union_pw_aff_read_from_str.argtypes = [Context, c_char_p]
isl.isl_multi_union_pw_aff_add.restype = c_void_p
isl.isl_multi_union_pw_aff_add.argtypes = [c_void_p, c_void_p]
isl.isl_multi_union_pw_aff_flat_range_product.restype = c_void_p
isl.isl_multi_union_pw_aff_flat_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_union_pw_aff_pullback_union_pw_multi_aff.restype = c_void_p
isl.isl_multi_union_pw_aff_pullback_union_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_multi_union_pw_aff_range_product.restype = c_void_p
isl.isl_multi_union_pw_aff_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_union_pw_aff_union_add.restype = c_void_p
isl.isl_multi_union_pw_aff_union_add.argtypes = [c_void_p, c_void_p]
isl.isl_multi_union_pw_aff_copy.restype = c_void_p
isl.isl_multi_union_pw_aff_copy.argtypes = [c_void_p]
isl.isl_multi_union_pw_aff_free.restype = c_void_p
isl.isl_multi_union_pw_aff_free.argtypes = [c_void_p]
isl.isl_multi_union_pw_aff_to_str.restype = POINTER(c_char)
isl.isl_multi_union_pw_aff_to_str.argtypes = [c_void_p]

class union_pw_aff(union_pw_multi_aff, multi_union_pw_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_aff_from_pw_aff(isl.isl_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_aff_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_pw_aff_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is union_pw_aff:
                arg0 = union_pw_aff(arg0)
        except:
            raise
        ptr = isl.isl_union_pw_aff_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_pw_aff("""%s""")' % s
        else:
            return 'isl.union_pw_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_aff:
                arg0 = union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_aff:
                arg1 = union_pw_aff(arg1)
        except:
            return union_pw_multi_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_union_pw_aff_add(isl.isl_union_pw_aff_copy(arg0.ptr), isl.isl_union_pw_aff_copy(arg1.ptr))
        obj = union_pw_aff(ctx=ctx, ptr=res)
        return obj
    def pullback(arg0, arg1):
        if arg1.__class__ is union_pw_multi_aff:
            res = isl.isl_union_pw_aff_pullback_union_pw_multi_aff(isl.isl_union_pw_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = union_pw_aff(ctx=ctx, ptr=res)
            return obj
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_aff:
                arg0 = union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_aff:
                arg1 = union_pw_aff(arg1)
        except:
            return union_pw_multi_aff(arg0).union_add(arg1)
        ctx = arg0.ctx
        res = isl.isl_union_pw_aff_union_add(isl.isl_union_pw_aff_copy(arg0.ptr), isl.isl_union_pw_aff_copy(arg1.ptr))
        obj = union_pw_aff(ctx=ctx, ptr=res)
        return obj

isl.isl_union_pw_aff_from_pw_aff.restype = c_void_p
isl.isl_union_pw_aff_from_pw_aff.argtypes = [c_void_p]
isl.isl_union_pw_aff_read_from_str.restype = c_void_p
isl.isl_union_pw_aff_read_from_str.argtypes = [Context, c_char_p]
isl.isl_union_pw_aff_add.restype = c_void_p
isl.isl_union_pw_aff_add.argtypes = [c_void_p, c_void_p]
isl.isl_union_pw_aff_pullback_union_pw_multi_aff.restype = c_void_p
isl.isl_union_pw_aff_pullback_union_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_union_pw_aff_union_add.restype = c_void_p
isl.isl_union_pw_aff_union_add.argtypes = [c_void_p, c_void_p]
isl.isl_union_pw_aff_copy.restype = c_void_p
isl.isl_union_pw_aff_copy.argtypes = [c_void_p]
isl.isl_union_pw_aff_free.restype = c_void_p
isl.isl_union_pw_aff_free.argtypes = [c_void_p]
isl.isl_union_pw_aff_to_str.restype = POINTER(c_char)
isl.isl_union_pw_aff_to_str.argtypes = [c_void_p]

class multi_pw_aff(multi_union_pw_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is multi_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_pw_aff_from_multi_aff(isl.isl_multi_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_pw_aff_from_pw_aff(isl.isl_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is pw_multi_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_pw_aff_from_pw_multi_aff(isl.isl_pw_multi_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_pw_aff_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_multi_pw_aff_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is multi_pw_aff:
                arg0 = multi_pw_aff(arg0)
        except:
            raise
        ptr = isl.isl_multi_pw_aff_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.multi_pw_aff("""%s""")' % s
        else:
            return 'isl.multi_pw_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_pw_aff:
                arg0 = multi_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_pw_aff:
                arg1 = multi_pw_aff(arg1)
        except:
            return multi_union_pw_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_pw_aff_add(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
        obj = multi_pw_aff(ctx=ctx, ptr=res)
        return obj
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_pw_aff:
                arg0 = multi_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_pw_aff:
                arg1 = multi_pw_aff(arg1)
        except:
            return multi_union_pw_aff(arg0).flat_range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_pw_aff_flat_range_product(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
        obj = multi_pw_aff(ctx=ctx, ptr=res)
        return obj
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_pw_aff:
                arg0 = multi_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_pw_aff:
                arg1 = multi_pw_aff(arg1)
        except:
            return multi_union_pw_aff(arg0).product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_pw_aff_product(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
        obj = multi_pw_aff(ctx=ctx, ptr=res)
        return obj
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_multi_pw_aff_pullback_multi_aff(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = multi_pw_aff(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is pw_multi_aff:
            res = isl.isl_multi_pw_aff_pullback_pw_multi_aff(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = multi_pw_aff(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is multi_pw_aff:
            res = isl.isl_multi_pw_aff_pullback_multi_pw_aff(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = multi_pw_aff(ctx=ctx, ptr=res)
            return obj
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_pw_aff:
                arg0 = multi_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_pw_aff:
                arg1 = multi_pw_aff(arg1)
        except:
            return multi_union_pw_aff(arg0).range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_pw_aff_range_product(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
        obj = multi_pw_aff(ctx=ctx, ptr=res)
        return obj

isl.isl_multi_pw_aff_from_multi_aff.restype = c_void_p
isl.isl_multi_pw_aff_from_multi_aff.argtypes = [c_void_p]
isl.isl_multi_pw_aff_from_pw_aff.restype = c_void_p
isl.isl_multi_pw_aff_from_pw_aff.argtypes = [c_void_p]
isl.isl_multi_pw_aff_from_pw_multi_aff.restype = c_void_p
isl.isl_multi_pw_aff_from_pw_multi_aff.argtypes = [c_void_p]
isl.isl_multi_pw_aff_read_from_str.restype = c_void_p
isl.isl_multi_pw_aff_read_from_str.argtypes = [Context, c_char_p]
isl.isl_multi_pw_aff_add.restype = c_void_p
isl.isl_multi_pw_aff_add.argtypes = [c_void_p, c_void_p]
isl.isl_multi_pw_aff_flat_range_product.restype = c_void_p
isl.isl_multi_pw_aff_flat_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_pw_aff_product.restype = c_void_p
isl.isl_multi_pw_aff_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_pw_aff_pullback_multi_aff.restype = c_void_p
isl.isl_multi_pw_aff_pullback_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_multi_pw_aff_pullback_pw_multi_aff.restype = c_void_p
isl.isl_multi_pw_aff_pullback_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_multi_pw_aff_pullback_multi_pw_aff.restype = c_void_p
isl.isl_multi_pw_aff_pullback_multi_pw_aff.argtypes = [c_void_p, c_void_p]
isl.isl_multi_pw_aff_range_product.restype = c_void_p
isl.isl_multi_pw_aff_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_pw_aff_copy.restype = c_void_p
isl.isl_multi_pw_aff_copy.argtypes = [c_void_p]
isl.isl_multi_pw_aff_free.restype = c_void_p
isl.isl_multi_pw_aff_free.argtypes = [c_void_p]
isl.isl_multi_pw_aff_to_str.restype = POINTER(c_char)
isl.isl_multi_pw_aff_to_str.argtypes = [c_void_p]

class pw_multi_aff(union_pw_multi_aff, multi_pw_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is multi_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_multi_aff_from_multi_aff(isl.isl_multi_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_multi_aff_from_pw_aff(isl.isl_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_multi_aff_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_pw_multi_aff_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        ptr = isl.isl_pw_multi_aff_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.pw_multi_aff("""%s""")' % s
        else:
            return 'isl.pw_multi_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return union_pw_multi_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_add(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        obj = pw_multi_aff(ctx=ctx, ptr=res)
        return obj
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return union_pw_multi_aff(arg0).flat_range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_flat_range_product(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        obj = pw_multi_aff(ctx=ctx, ptr=res)
        return obj
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return union_pw_multi_aff(arg0).product(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_product(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        obj = pw_multi_aff(ctx=ctx, ptr=res)
        return obj
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_pw_multi_aff_pullback_multi_aff(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = pw_multi_aff(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is pw_multi_aff:
            res = isl.isl_pw_multi_aff_pullback_pw_multi_aff(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = pw_multi_aff(ctx=ctx, ptr=res)
            return obj
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return union_pw_multi_aff(arg0).range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_range_product(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        obj = pw_multi_aff(ctx=ctx, ptr=res)
        return obj
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return union_pw_multi_aff(arg0).union_add(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_union_add(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        obj = pw_multi_aff(ctx=ctx, ptr=res)
        return obj

isl.isl_pw_multi_aff_from_multi_aff.restype = c_void_p
isl.isl_pw_multi_aff_from_multi_aff.argtypes = [c_void_p]
isl.isl_pw_multi_aff_from_pw_aff.restype = c_void_p
isl.isl_pw_multi_aff_from_pw_aff.argtypes = [c_void_p]
isl.isl_pw_multi_aff_read_from_str.restype = c_void_p
isl.isl_pw_multi_aff_read_from_str.argtypes = [Context, c_char_p]
isl.isl_pw_multi_aff_add.restype = c_void_p
isl.isl_pw_multi_aff_add.argtypes = [c_void_p, c_void_p]
isl.isl_pw_multi_aff_flat_range_product.restype = c_void_p
isl.isl_pw_multi_aff_flat_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_pw_multi_aff_product.restype = c_void_p
isl.isl_pw_multi_aff_product.argtypes = [c_void_p, c_void_p]
isl.isl_pw_multi_aff_pullback_multi_aff.restype = c_void_p
isl.isl_pw_multi_aff_pullback_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_pw_multi_aff_pullback_pw_multi_aff.restype = c_void_p
isl.isl_pw_multi_aff_pullback_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_pw_multi_aff_range_product.restype = c_void_p
isl.isl_pw_multi_aff_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_pw_multi_aff_union_add.restype = c_void_p
isl.isl_pw_multi_aff_union_add.argtypes = [c_void_p, c_void_p]
isl.isl_pw_multi_aff_copy.restype = c_void_p
isl.isl_pw_multi_aff_copy.argtypes = [c_void_p]
isl.isl_pw_multi_aff_free.restype = c_void_p
isl.isl_pw_multi_aff_free.argtypes = [c_void_p]
isl.isl_pw_multi_aff_to_str.restype = POINTER(c_char)
isl.isl_pw_multi_aff_to_str.argtypes = [c_void_p]

class pw_aff(union_pw_aff, pw_multi_aff, multi_pw_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_aff_from_aff(isl.isl_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_aff_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_pw_aff_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        ptr = isl.isl_pw_aff_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.pw_aff("""%s""")' % s
        else:
            return 'isl.pw_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_add(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def ceil(arg0):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_pw_aff_ceil(isl.isl_pw_aff_copy(arg0.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def cond(arg0, arg1, arg2):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).cond(arg1, arg2)
        try:
            if not arg2.__class__ is pw_aff:
                arg2 = pw_aff(arg2)
        except:
            return union_pw_aff(arg0).cond(arg1, arg2)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_cond(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr), isl.isl_pw_aff_copy(arg2.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def div(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).div(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_div(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def domain(arg0):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_pw_aff_domain(isl.isl_pw_aff_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def eq_set(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).eq_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_eq_set(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def floor(arg0):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_pw_aff_floor(isl.isl_pw_aff_copy(arg0.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def ge_set(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).ge_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_ge_set(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def gt_set(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).gt_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_gt_set(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def le_set(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).le_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_le_set(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def lt_set(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).lt_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_lt_set(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def max(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).max(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_max(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def min(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).min(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_min(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def mod(arg0, arg1):
        if arg1.__class__ is val:
            res = isl.isl_pw_aff_mod_val(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = pw_aff(ctx=ctx, ptr=res)
            return obj
    def mul(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).mul(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_mul(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def ne_set(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).ne_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_ne_set(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def neg(arg0):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_pw_aff_neg(isl.isl_pw_aff_copy(arg0.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_pw_aff_pullback_multi_aff(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = pw_aff(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is pw_multi_aff:
            res = isl.isl_pw_aff_pullback_pw_multi_aff(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = pw_aff(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is multi_pw_aff:
            res = isl.isl_pw_aff_pullback_multi_pw_aff(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = pw_aff(ctx=ctx, ptr=res)
            return obj
    def scale(arg0, arg1):
        if arg1.__class__ is val:
            res = isl.isl_pw_aff_scale_val(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = pw_aff(ctx=ctx, ptr=res)
            return obj
    def scale_down(arg0, arg1):
        if arg1.__class__ is val:
            res = isl.isl_pw_aff_scale_down_val(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = pw_aff(ctx=ctx, ptr=res)
            return obj
    def sub(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).sub(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_sub(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def tdiv_q(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).tdiv_q(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_tdiv_q(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def tdiv_r(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).tdiv_r(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_tdiv_r(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).union_add(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_union_add(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        obj = pw_aff(ctx=ctx, ptr=res)
        return obj

isl.isl_pw_aff_from_aff.restype = c_void_p
isl.isl_pw_aff_from_aff.argtypes = [c_void_p]
isl.isl_pw_aff_read_from_str.restype = c_void_p
isl.isl_pw_aff_read_from_str.argtypes = [Context, c_char_p]
isl.isl_pw_aff_add.restype = c_void_p
isl.isl_pw_aff_add.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_ceil.restype = c_void_p
isl.isl_pw_aff_ceil.argtypes = [c_void_p]
isl.isl_pw_aff_cond.restype = c_void_p
isl.isl_pw_aff_cond.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_pw_aff_div.restype = c_void_p
isl.isl_pw_aff_div.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_domain.restype = c_void_p
isl.isl_pw_aff_domain.argtypes = [c_void_p]
isl.isl_pw_aff_eq_set.restype = c_void_p
isl.isl_pw_aff_eq_set.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_floor.restype = c_void_p
isl.isl_pw_aff_floor.argtypes = [c_void_p]
isl.isl_pw_aff_ge_set.restype = c_void_p
isl.isl_pw_aff_ge_set.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_gt_set.restype = c_void_p
isl.isl_pw_aff_gt_set.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_le_set.restype = c_void_p
isl.isl_pw_aff_le_set.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_lt_set.restype = c_void_p
isl.isl_pw_aff_lt_set.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_max.restype = c_void_p
isl.isl_pw_aff_max.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_min.restype = c_void_p
isl.isl_pw_aff_min.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_mod_val.restype = c_void_p
isl.isl_pw_aff_mod_val.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_mul.restype = c_void_p
isl.isl_pw_aff_mul.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_ne_set.restype = c_void_p
isl.isl_pw_aff_ne_set.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_neg.restype = c_void_p
isl.isl_pw_aff_neg.argtypes = [c_void_p]
isl.isl_pw_aff_pullback_multi_aff.restype = c_void_p
isl.isl_pw_aff_pullback_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_pullback_pw_multi_aff.restype = c_void_p
isl.isl_pw_aff_pullback_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_pullback_multi_pw_aff.restype = c_void_p
isl.isl_pw_aff_pullback_multi_pw_aff.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_scale_val.restype = c_void_p
isl.isl_pw_aff_scale_val.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_scale_down_val.restype = c_void_p
isl.isl_pw_aff_scale_down_val.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_sub.restype = c_void_p
isl.isl_pw_aff_sub.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_tdiv_q.restype = c_void_p
isl.isl_pw_aff_tdiv_q.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_tdiv_r.restype = c_void_p
isl.isl_pw_aff_tdiv_r.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_union_add.restype = c_void_p
isl.isl_pw_aff_union_add.argtypes = [c_void_p, c_void_p]
isl.isl_pw_aff_copy.restype = c_void_p
isl.isl_pw_aff_copy.argtypes = [c_void_p]
isl.isl_pw_aff_free.restype = c_void_p
isl.isl_pw_aff_free.argtypes = [c_void_p]
isl.isl_pw_aff_to_str.restype = POINTER(c_char)
isl.isl_pw_aff_to_str.argtypes = [c_void_p]

class multi_aff(pw_multi_aff, multi_pw_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_aff_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        if len(args) == 1 and args[0].__class__ is aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_aff_from_aff(isl.isl_aff_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_multi_aff_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is multi_aff:
                arg0 = multi_aff(arg0)
        except:
            raise
        ptr = isl.isl_multi_aff_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.multi_aff("""%s""")' % s
        else:
            return 'isl.multi_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_aff:
                arg0 = multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_aff:
                arg1 = multi_aff(arg1)
        except:
            return pw_multi_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_aff_add(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
        obj = multi_aff(ctx=ctx, ptr=res)
        return obj
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_aff:
                arg0 = multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_aff:
                arg1 = multi_aff(arg1)
        except:
            return pw_multi_aff(arg0).flat_range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_aff_flat_range_product(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
        obj = multi_aff(ctx=ctx, ptr=res)
        return obj
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_aff:
                arg0 = multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_aff:
                arg1 = multi_aff(arg1)
        except:
            return pw_multi_aff(arg0).product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_aff_product(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
        obj = multi_aff(ctx=ctx, ptr=res)
        return obj
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_multi_aff_pullback_multi_aff(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = multi_aff(ctx=ctx, ptr=res)
            return obj
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_aff:
                arg0 = multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_aff:
                arg1 = multi_aff(arg1)
        except:
            return pw_multi_aff(arg0).range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_aff_range_product(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
        obj = multi_aff(ctx=ctx, ptr=res)
        return obj

isl.isl_multi_aff_read_from_str.restype = c_void_p
isl.isl_multi_aff_read_from_str.argtypes = [Context, c_char_p]
isl.isl_multi_aff_from_aff.restype = c_void_p
isl.isl_multi_aff_from_aff.argtypes = [c_void_p]
isl.isl_multi_aff_add.restype = c_void_p
isl.isl_multi_aff_add.argtypes = [c_void_p, c_void_p]
isl.isl_multi_aff_flat_range_product.restype = c_void_p
isl.isl_multi_aff_flat_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_aff_product.restype = c_void_p
isl.isl_multi_aff_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_aff_pullback_multi_aff.restype = c_void_p
isl.isl_multi_aff_pullback_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_multi_aff_range_product.restype = c_void_p
isl.isl_multi_aff_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_aff_copy.restype = c_void_p
isl.isl_multi_aff_copy.argtypes = [c_void_p]
isl.isl_multi_aff_free.restype = c_void_p
isl.isl_multi_aff_free.argtypes = [c_void_p]
isl.isl_multi_aff_to_str.restype = POINTER(c_char)
isl.isl_multi_aff_to_str.argtypes = [c_void_p]

class aff(pw_aff, multi_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_aff_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_aff_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        ptr = isl.isl_aff_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.aff("""%s""")' % s
        else:
            return 'isl.aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_add(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = aff(ctx=ctx, ptr=res)
        return obj
    def ceil(arg0):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_aff_ceil(isl.isl_aff_copy(arg0.ptr))
        obj = aff(ctx=ctx, ptr=res)
        return obj
    def div(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).div(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_div(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = aff(ctx=ctx, ptr=res)
        return obj
    def eq_set(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).eq_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_eq_set(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def floor(arg0):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_aff_floor(isl.isl_aff_copy(arg0.ptr))
        obj = aff(ctx=ctx, ptr=res)
        return obj
    def ge_set(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).ge_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_ge_set(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def gt_set(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).gt_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_gt_set(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def le_set(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).le_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_le_set(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def lt_set(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).lt_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_lt_set(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def mod(arg0, arg1):
        if arg1.__class__ is val:
            res = isl.isl_aff_mod_val(isl.isl_aff_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = aff(ctx=ctx, ptr=res)
            return obj
    def mul(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).mul(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_mul(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = aff(ctx=ctx, ptr=res)
        return obj
    def ne_set(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).ne_set(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_ne_set(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def neg(arg0):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_aff_neg(isl.isl_aff_copy(arg0.ptr))
        obj = aff(ctx=ctx, ptr=res)
        return obj
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_aff_pullback_multi_aff(isl.isl_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = aff(ctx=ctx, ptr=res)
            return obj
    def scale(arg0, arg1):
        if arg1.__class__ is val:
            res = isl.isl_aff_scale_val(isl.isl_aff_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = aff(ctx=ctx, ptr=res)
            return obj
    def scale_down(arg0, arg1):
        if arg1.__class__ is val:
            res = isl.isl_aff_scale_down_val(isl.isl_aff_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = aff(ctx=ctx, ptr=res)
            return obj
    def sub(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).sub(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_sub(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        obj = aff(ctx=ctx, ptr=res)
        return obj

isl.isl_aff_read_from_str.restype = c_void_p
isl.isl_aff_read_from_str.argtypes = [Context, c_char_p]
isl.isl_aff_add.restype = c_void_p
isl.isl_aff_add.argtypes = [c_void_p, c_void_p]
isl.isl_aff_ceil.restype = c_void_p
isl.isl_aff_ceil.argtypes = [c_void_p]
isl.isl_aff_div.restype = c_void_p
isl.isl_aff_div.argtypes = [c_void_p, c_void_p]
isl.isl_aff_eq_set.restype = c_void_p
isl.isl_aff_eq_set.argtypes = [c_void_p, c_void_p]
isl.isl_aff_floor.restype = c_void_p
isl.isl_aff_floor.argtypes = [c_void_p]
isl.isl_aff_ge_set.restype = c_void_p
isl.isl_aff_ge_set.argtypes = [c_void_p, c_void_p]
isl.isl_aff_gt_set.restype = c_void_p
isl.isl_aff_gt_set.argtypes = [c_void_p, c_void_p]
isl.isl_aff_le_set.restype = c_void_p
isl.isl_aff_le_set.argtypes = [c_void_p, c_void_p]
isl.isl_aff_lt_set.restype = c_void_p
isl.isl_aff_lt_set.argtypes = [c_void_p, c_void_p]
isl.isl_aff_mod_val.restype = c_void_p
isl.isl_aff_mod_val.argtypes = [c_void_p, c_void_p]
isl.isl_aff_mul.restype = c_void_p
isl.isl_aff_mul.argtypes = [c_void_p, c_void_p]
isl.isl_aff_ne_set.restype = c_void_p
isl.isl_aff_ne_set.argtypes = [c_void_p, c_void_p]
isl.isl_aff_neg.restype = c_void_p
isl.isl_aff_neg.argtypes = [c_void_p]
isl.isl_aff_pullback_multi_aff.restype = c_void_p
isl.isl_aff_pullback_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_aff_scale_val.restype = c_void_p
isl.isl_aff_scale_val.argtypes = [c_void_p, c_void_p]
isl.isl_aff_scale_down_val.restype = c_void_p
isl.isl_aff_scale_down_val.argtypes = [c_void_p, c_void_p]
isl.isl_aff_sub.restype = c_void_p
isl.isl_aff_sub.argtypes = [c_void_p, c_void_p]
isl.isl_aff_copy.restype = c_void_p
isl.isl_aff_copy.argtypes = [c_void_p]
isl.isl_aff_free.restype = c_void_p
isl.isl_aff_free.argtypes = [c_void_p]
isl.isl_aff_to_str.restype = POINTER(c_char)
isl.isl_aff_to_str.argtypes = [c_void_p]

class ast_build(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 0:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_ast_build_alloc(self.ctx)
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_build_free(self.ptr)
    def copy_callbacks(self, obj):
        if hasattr(obj, 'at_each_domain'):
            self.at_each_domain = obj.at_each_domain
    def set_at_each_domain(arg0, arg1):
        try:
            if not arg0.__class__ is ast_build:
                arg0 = ast_build(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1, cb_arg2):
            cb_arg0 = ast_node(ctx=arg0.ctx, ptr=(cb_arg0))
            cb_arg1 = ast_build(ctx=arg0.ctx, ptr=isl.isl_ast_build_copy(cb_arg1))
            try:
                res = arg1(cb_arg0, cb_arg1)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return None
            return isl.isl_ast_node_copy(res.ptr)
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_ast_build_set_at_each_domain(isl.isl_ast_build_copy(arg0.ptr), cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if hasattr(arg0, 'at_each_domain') and arg0.at_each_domain['exc_info'] != None:
            exc_info = arg0.at_each_domain['exc_info'][0]
            arg0.at_each_domain['exc_info'][0] = None
            if exc_info != None:
                raise (exc_info[0], exc_info[1], exc_info[2])
        obj = ast_build(ctx=ctx, ptr=res)
        obj.copy_callbacks(arg0)
        obj.at_each_domain = { 'func': cb, 'exc_info': exc_info }
        return obj
    def access_from(arg0, arg1):
        if arg1.__class__ is pw_multi_aff:
            res = isl.isl_ast_build_access_from_pw_multi_aff(arg0.ptr, isl.isl_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            if hasattr(arg0, 'at_each_domain') and arg0.at_each_domain['exc_info'] != None:
                exc_info = arg0.at_each_domain['exc_info'][0]
                arg0.at_each_domain['exc_info'][0] = None
                if exc_info != None:
                    raise (exc_info[0], exc_info[1], exc_info[2])
            obj = ast_expr(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is multi_pw_aff:
            res = isl.isl_ast_build_access_from_multi_pw_aff(arg0.ptr, isl.isl_multi_pw_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            if hasattr(arg0, 'at_each_domain') and arg0.at_each_domain['exc_info'] != None:
                exc_info = arg0.at_each_domain['exc_info'][0]
                arg0.at_each_domain['exc_info'][0] = None
                if exc_info != None:
                    raise (exc_info[0], exc_info[1], exc_info[2])
            obj = ast_expr(ctx=ctx, ptr=res)
            return obj
    def call_from(arg0, arg1):
        if arg1.__class__ is pw_multi_aff:
            res = isl.isl_ast_build_call_from_pw_multi_aff(arg0.ptr, isl.isl_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            if hasattr(arg0, 'at_each_domain') and arg0.at_each_domain['exc_info'] != None:
                exc_info = arg0.at_each_domain['exc_info'][0]
                arg0.at_each_domain['exc_info'][0] = None
                if exc_info != None:
                    raise (exc_info[0], exc_info[1], exc_info[2])
            obj = ast_expr(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is multi_pw_aff:
            res = isl.isl_ast_build_call_from_multi_pw_aff(arg0.ptr, isl.isl_multi_pw_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            if hasattr(arg0, 'at_each_domain') and arg0.at_each_domain['exc_info'] != None:
                exc_info = arg0.at_each_domain['exc_info'][0]
                arg0.at_each_domain['exc_info'][0] = None
                if exc_info != None:
                    raise (exc_info[0], exc_info[1], exc_info[2])
            obj = ast_expr(ctx=ctx, ptr=res)
            return obj
    def expr_from(arg0, arg1):
        if arg1.__class__ is set:
            res = isl.isl_ast_build_expr_from_set(arg0.ptr, isl.isl_set_copy(arg1.ptr))
            ctx = arg0.ctx
            if hasattr(arg0, 'at_each_domain') and arg0.at_each_domain['exc_info'] != None:
                exc_info = arg0.at_each_domain['exc_info'][0]
                arg0.at_each_domain['exc_info'][0] = None
                if exc_info != None:
                    raise (exc_info[0], exc_info[1], exc_info[2])
            obj = ast_expr(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is pw_aff:
            res = isl.isl_ast_build_expr_from_pw_aff(arg0.ptr, isl.isl_pw_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            if hasattr(arg0, 'at_each_domain') and arg0.at_each_domain['exc_info'] != None:
                exc_info = arg0.at_each_domain['exc_info'][0]
                arg0.at_each_domain['exc_info'][0] = None
                if exc_info != None:
                    raise (exc_info[0], exc_info[1], exc_info[2])
            obj = ast_expr(ctx=ctx, ptr=res)
            return obj
    @staticmethod
    def from_context(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_build_from_context(isl.isl_set_copy(arg0.ptr))
        obj = ast_build(ctx=ctx, ptr=res)
        return obj
    def node_from(arg0, arg1):
        if arg1.__class__ is schedule:
            res = isl.isl_ast_build_node_from_schedule(arg0.ptr, isl.isl_schedule_copy(arg1.ptr))
            ctx = arg0.ctx
            if hasattr(arg0, 'at_each_domain') and arg0.at_each_domain['exc_info'] != None:
                exc_info = arg0.at_each_domain['exc_info'][0]
                arg0.at_each_domain['exc_info'][0] = None
                if exc_info != None:
                    raise (exc_info[0], exc_info[1], exc_info[2])
            obj = ast_node(ctx=ctx, ptr=res)
            return obj
    def node_from_schedule_map(arg0, arg1):
        try:
            if not arg0.__class__ is ast_build:
                arg0 = ast_build(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_build_node_from_schedule_map(arg0.ptr, isl.isl_union_map_copy(arg1.ptr))
        if hasattr(arg0, 'at_each_domain') and arg0.at_each_domain['exc_info'] != None:
            exc_info = arg0.at_each_domain['exc_info'][0]
            arg0.at_each_domain['exc_info'][0] = None
            if exc_info != None:
                raise (exc_info[0], exc_info[1], exc_info[2])
        obj = ast_node(ctx=ctx, ptr=res)
        return obj

isl.isl_ast_build_alloc.restype = c_void_p
isl.isl_ast_build_alloc.argtypes = [Context]
isl.isl_ast_build_set_at_each_domain.restype = c_void_p
isl.isl_ast_build_set_at_each_domain.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_ast_build_access_from_pw_multi_aff.restype = c_void_p
isl.isl_ast_build_access_from_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_ast_build_access_from_multi_pw_aff.restype = c_void_p
isl.isl_ast_build_access_from_multi_pw_aff.argtypes = [c_void_p, c_void_p]
isl.isl_ast_build_call_from_pw_multi_aff.restype = c_void_p
isl.isl_ast_build_call_from_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_ast_build_call_from_multi_pw_aff.restype = c_void_p
isl.isl_ast_build_call_from_multi_pw_aff.argtypes = [c_void_p, c_void_p]
isl.isl_ast_build_expr_from_set.restype = c_void_p
isl.isl_ast_build_expr_from_set.argtypes = [c_void_p, c_void_p]
isl.isl_ast_build_expr_from_pw_aff.restype = c_void_p
isl.isl_ast_build_expr_from_pw_aff.argtypes = [c_void_p, c_void_p]
isl.isl_ast_build_from_context.restype = c_void_p
isl.isl_ast_build_from_context.argtypes = [c_void_p]
isl.isl_ast_build_node_from_schedule.restype = c_void_p
isl.isl_ast_build_node_from_schedule.argtypes = [c_void_p, c_void_p]
isl.isl_ast_build_node_from_schedule_map.restype = c_void_p
isl.isl_ast_build_node_from_schedule_map.argtypes = [c_void_p, c_void_p]
isl.isl_ast_build_copy.restype = c_void_p
isl.isl_ast_build_copy.argtypes = [c_void_p]
isl.isl_ast_build_free.restype = c_void_p
isl.isl_ast_build_free.argtypes = [c_void_p]

class ast_expr(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_id):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_int):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        if "ptr" in keywords:
            type = isl.isl_ast_expr_get_type(keywords["ptr"])
            if type == 0:
                return ast_expr_op(**keywords)
            if type == 1:
                return ast_expr_id(**keywords)
            if type == 2:
                return ast_expr_int(**keywords)
            raise
        return super(ast_expr, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr:
                arg0 = ast_expr(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr("""%s""")' % s
        else:
            return 'isl.ast_expr("%s")' % s
    def to_C_str(arg0):
        try:
            if not arg0.__class__ is ast_expr:
                arg0 = ast_expr(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_expr_to_C_str(arg0.ptr)
        if res == 0:
            raise
        string = cast(res, c_char_p).value.decode('ascii')
        libc.free(res)
        return string

isl.isl_ast_expr_to_C_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_C_str.argtypes = [c_void_p]
isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]
isl.isl_ast_expr_get_type.argtypes = [c_void_p]

class ast_expr_id(ast_expr):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_id, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_id:
                arg0 = ast_expr_id(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_id("""%s""")' % s
        else:
            return 'isl.ast_expr_id("%s")' % s
    def id(arg0):
        try:
            if not arg0.__class__ is ast_expr:
                arg0 = ast_expr(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_expr_id_get_id(arg0.ptr)
        obj = id(ctx=ctx, ptr=res)
        return obj
    def get_id(arg0):
        return arg0.id()

isl.isl_ast_expr_id_get_id.restype = c_void_p
isl.isl_ast_expr_id_get_id.argtypes = [c_void_p]
isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_int(ast_expr):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_int, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_int:
                arg0 = ast_expr_int(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_int("""%s""")' % s
        else:
            return 'isl.ast_expr_int("%s")' % s
    def val(arg0):
        try:
            if not arg0.__class__ is ast_expr:
                arg0 = ast_expr(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_expr_int_get_val(arg0.ptr)
        obj = val(ctx=ctx, ptr=res)
        return obj
    def get_val(arg0):
        return arg0.val()

isl.isl_ast_expr_int_get_val.restype = c_void_p
isl.isl_ast_expr_int_get_val.argtypes = [c_void_p]
isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op(ast_expr):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_and):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_and_then):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_or):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_or_else):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_max):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_min):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_minus):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_add):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_sub):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_mul):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_div):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_fdiv_q):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_pdiv_q):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_pdiv_r):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_zdiv_r):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_cond):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_select):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_eq):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_le):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_lt):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_ge):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_gt):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_call):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_access):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_member):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_expr_op_address_of):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_expr_copy(args[0].ptr)
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        if "ptr" in keywords:
            type = isl.isl_ast_expr_op_get_type(keywords["ptr"])
            if type == 0:
                return ast_expr_op_and(**keywords)
            if type == 1:
                return ast_expr_op_and_then(**keywords)
            if type == 2:
                return ast_expr_op_or(**keywords)
            if type == 3:
                return ast_expr_op_or_else(**keywords)
            if type == 4:
                return ast_expr_op_max(**keywords)
            if type == 5:
                return ast_expr_op_min(**keywords)
            if type == 6:
                return ast_expr_op_minus(**keywords)
            if type == 7:
                return ast_expr_op_add(**keywords)
            if type == 8:
                return ast_expr_op_sub(**keywords)
            if type == 9:
                return ast_expr_op_mul(**keywords)
            if type == 10:
                return ast_expr_op_div(**keywords)
            if type == 11:
                return ast_expr_op_fdiv_q(**keywords)
            if type == 12:
                return ast_expr_op_pdiv_q(**keywords)
            if type == 13:
                return ast_expr_op_pdiv_r(**keywords)
            if type == 14:
                return ast_expr_op_zdiv_r(**keywords)
            if type == 15:
                return ast_expr_op_cond(**keywords)
            if type == 16:
                return ast_expr_op_select(**keywords)
            if type == 17:
                return ast_expr_op_eq(**keywords)
            if type == 18:
                return ast_expr_op_le(**keywords)
            if type == 19:
                return ast_expr_op_lt(**keywords)
            if type == 20:
                return ast_expr_op_ge(**keywords)
            if type == 21:
                return ast_expr_op_gt(**keywords)
            if type == 22:
                return ast_expr_op_call(**keywords)
            if type == 23:
                return ast_expr_op_access(**keywords)
            if type == 24:
                return ast_expr_op_member(**keywords)
            if type == 25:
                return ast_expr_op_address_of(**keywords)
            raise
        return super(ast_expr_op, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op:
                arg0 = ast_expr_op(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op("""%s""")' % s
        else:
            return 'isl.ast_expr_op("%s")' % s
    def arg(arg0, arg1):
        try:
            if not arg0.__class__ is ast_expr:
                arg0 = ast_expr(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_expr_op_get_arg(arg0.ptr, arg1)
        obj = ast_expr(ctx=ctx, ptr=res)
        return obj
    def get_arg(arg0, arg1):
        return arg0.arg(arg1)
    def n_arg(arg0):
        try:
            if not arg0.__class__ is ast_expr:
                arg0 = ast_expr(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_expr_op_get_n_arg(arg0.ptr)
        if res < 0:
            raise
        return int(res)
    def get_n_arg(arg0):
        return arg0.n_arg()

isl.isl_ast_expr_op_get_arg.restype = c_void_p
isl.isl_ast_expr_op_get_arg.argtypes = [c_void_p, c_int]
isl.isl_ast_expr_op_get_n_arg.argtypes = [c_void_p]
isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]
isl.isl_ast_expr_op_get_type.argtypes = [c_void_p]

class ast_expr_op_access(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_access, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_access:
                arg0 = ast_expr_op_access(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_access("""%s""")' % s
        else:
            return 'isl.ast_expr_op_access("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_add(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_add, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_add:
                arg0 = ast_expr_op_add(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_add("""%s""")' % s
        else:
            return 'isl.ast_expr_op_add("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_address_of(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_address_of, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_address_of:
                arg0 = ast_expr_op_address_of(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_address_of("""%s""")' % s
        else:
            return 'isl.ast_expr_op_address_of("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_and(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_and, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_and:
                arg0 = ast_expr_op_and(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_and("""%s""")' % s
        else:
            return 'isl.ast_expr_op_and("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_and_then(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_and_then, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_and_then:
                arg0 = ast_expr_op_and_then(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_and_then("""%s""")' % s
        else:
            return 'isl.ast_expr_op_and_then("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_call(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_call, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_call:
                arg0 = ast_expr_op_call(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_call("""%s""")' % s
        else:
            return 'isl.ast_expr_op_call("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_cond(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_cond, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_cond:
                arg0 = ast_expr_op_cond(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_cond("""%s""")' % s
        else:
            return 'isl.ast_expr_op_cond("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_div(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_div, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_div:
                arg0 = ast_expr_op_div(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_div("""%s""")' % s
        else:
            return 'isl.ast_expr_op_div("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_eq(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_eq, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_eq:
                arg0 = ast_expr_op_eq(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_eq("""%s""")' % s
        else:
            return 'isl.ast_expr_op_eq("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_fdiv_q(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_fdiv_q, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_fdiv_q:
                arg0 = ast_expr_op_fdiv_q(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_fdiv_q("""%s""")' % s
        else:
            return 'isl.ast_expr_op_fdiv_q("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_ge(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_ge, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_ge:
                arg0 = ast_expr_op_ge(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_ge("""%s""")' % s
        else:
            return 'isl.ast_expr_op_ge("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_gt(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_gt, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_gt:
                arg0 = ast_expr_op_gt(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_gt("""%s""")' % s
        else:
            return 'isl.ast_expr_op_gt("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_le(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_le, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_le:
                arg0 = ast_expr_op_le(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_le("""%s""")' % s
        else:
            return 'isl.ast_expr_op_le("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_lt(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_lt, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_lt:
                arg0 = ast_expr_op_lt(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_lt("""%s""")' % s
        else:
            return 'isl.ast_expr_op_lt("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_max(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_max, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_max:
                arg0 = ast_expr_op_max(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_max("""%s""")' % s
        else:
            return 'isl.ast_expr_op_max("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_member(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_member, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_member:
                arg0 = ast_expr_op_member(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_member("""%s""")' % s
        else:
            return 'isl.ast_expr_op_member("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_min(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_min, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_min:
                arg0 = ast_expr_op_min(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_min("""%s""")' % s
        else:
            return 'isl.ast_expr_op_min("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_minus(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_minus, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_minus:
                arg0 = ast_expr_op_minus(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_minus("""%s""")' % s
        else:
            return 'isl.ast_expr_op_minus("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_mul(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_mul, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_mul:
                arg0 = ast_expr_op_mul(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_mul("""%s""")' % s
        else:
            return 'isl.ast_expr_op_mul("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_or(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_or, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_or:
                arg0 = ast_expr_op_or(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_or("""%s""")' % s
        else:
            return 'isl.ast_expr_op_or("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_or_else(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_or_else, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_or_else:
                arg0 = ast_expr_op_or_else(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_or_else("""%s""")' % s
        else:
            return 'isl.ast_expr_op_or_else("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_pdiv_q(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_pdiv_q, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_pdiv_q:
                arg0 = ast_expr_op_pdiv_q(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_pdiv_q("""%s""")' % s
        else:
            return 'isl.ast_expr_op_pdiv_q("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_pdiv_r(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_pdiv_r, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_pdiv_r:
                arg0 = ast_expr_op_pdiv_r(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_pdiv_r("""%s""")' % s
        else:
            return 'isl.ast_expr_op_pdiv_r("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_select(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_select, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_select:
                arg0 = ast_expr_op_select(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_select("""%s""")' % s
        else:
            return 'isl.ast_expr_op_select("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_sub(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_sub, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_sub:
                arg0 = ast_expr_op_sub(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_sub("""%s""")' % s
        else:
            return 'isl.ast_expr_op_sub("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_expr_op_zdiv_r(ast_expr_op):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_expr_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_expr_op_zdiv_r, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_expr_op_zdiv_r:
                arg0 = ast_expr_op_zdiv_r(arg0)
        except:
            raise
        ptr = isl.isl_ast_expr_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_expr_op_zdiv_r("""%s""")' % s
        else:
            return 'isl.ast_expr_op_zdiv_r("%s")' % s

isl.isl_ast_expr_copy.restype = c_void_p
isl.isl_ast_expr_copy.argtypes = [c_void_p]
isl.isl_ast_expr_free.restype = c_void_p
isl.isl_ast_expr_free.argtypes = [c_void_p]
isl.isl_ast_expr_to_str.restype = POINTER(c_char)
isl.isl_ast_expr_to_str.argtypes = [c_void_p]

class ast_node(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and isinstance(args[0], ast_node_for):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_node_if):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_node_block):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_node_mark):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], ast_node_user):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_ast_node_copy(args[0].ptr)
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        if "ptr" in keywords:
            type = isl.isl_ast_node_get_type(keywords["ptr"])
            if type == 1:
                return ast_node_for(**keywords)
            if type == 2:
                return ast_node_if(**keywords)
            if type == 3:
                return ast_node_block(**keywords)
            if type == 4:
                return ast_node_mark(**keywords)
            if type == 5:
                return ast_node_user(**keywords)
            raise
        return super(ast_node, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ptr = isl.isl_ast_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_node("""%s""")' % s
        else:
            return 'isl.ast_node("%s")' % s
    def to_C_str(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_to_C_str(arg0.ptr)
        if res == 0:
            raise
        string = cast(res, c_char_p).value.decode('ascii')
        libc.free(res)
        return string

isl.isl_ast_node_to_C_str.restype = POINTER(c_char)
isl.isl_ast_node_to_C_str.argtypes = [c_void_p]
isl.isl_ast_node_copy.restype = c_void_p
isl.isl_ast_node_copy.argtypes = [c_void_p]
isl.isl_ast_node_free.restype = c_void_p
isl.isl_ast_node_free.argtypes = [c_void_p]
isl.isl_ast_node_to_str.restype = POINTER(c_char)
isl.isl_ast_node_to_str.argtypes = [c_void_p]
isl.isl_ast_node_get_type.argtypes = [c_void_p]

class ast_node_block(ast_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_node_block, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_node_block:
                arg0 = ast_node_block(arg0)
        except:
            raise
        ptr = isl.isl_ast_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_node_block("""%s""")' % s
        else:
            return 'isl.ast_node_block("%s")' % s
    def children(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_block_get_children(arg0.ptr)
        obj = ast_node_list(ctx=ctx, ptr=res)
        return obj
    def get_children(arg0):
        return arg0.children()

isl.isl_ast_node_block_get_children.restype = c_void_p
isl.isl_ast_node_block_get_children.argtypes = [c_void_p]
isl.isl_ast_node_copy.restype = c_void_p
isl.isl_ast_node_copy.argtypes = [c_void_p]
isl.isl_ast_node_free.restype = c_void_p
isl.isl_ast_node_free.argtypes = [c_void_p]
isl.isl_ast_node_to_str.restype = POINTER(c_char)
isl.isl_ast_node_to_str.argtypes = [c_void_p]

class ast_node_for(ast_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_node_for, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_node_for:
                arg0 = ast_node_for(arg0)
        except:
            raise
        ptr = isl.isl_ast_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_node_for("""%s""")' % s
        else:
            return 'isl.ast_node_for("%s")' % s
    def body(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_for_get_body(arg0.ptr)
        obj = ast_node(ctx=ctx, ptr=res)
        return obj
    def get_body(arg0):
        return arg0.body()
    def cond(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_for_get_cond(arg0.ptr)
        obj = ast_expr(ctx=ctx, ptr=res)
        return obj
    def get_cond(arg0):
        return arg0.cond()
    def inc(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_for_get_inc(arg0.ptr)
        obj = ast_expr(ctx=ctx, ptr=res)
        return obj
    def get_inc(arg0):
        return arg0.inc()
    def init(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_for_get_init(arg0.ptr)
        obj = ast_expr(ctx=ctx, ptr=res)
        return obj
    def get_init(arg0):
        return arg0.init()
    def iterator(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_for_get_iterator(arg0.ptr)
        obj = ast_expr(ctx=ctx, ptr=res)
        return obj
    def get_iterator(arg0):
        return arg0.iterator()
    def is_degenerate(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_for_is_degenerate(arg0.ptr)
        if res < 0:
            raise
        return bool(res)

isl.isl_ast_node_for_get_body.restype = c_void_p
isl.isl_ast_node_for_get_body.argtypes = [c_void_p]
isl.isl_ast_node_for_get_cond.restype = c_void_p
isl.isl_ast_node_for_get_cond.argtypes = [c_void_p]
isl.isl_ast_node_for_get_inc.restype = c_void_p
isl.isl_ast_node_for_get_inc.argtypes = [c_void_p]
isl.isl_ast_node_for_get_init.restype = c_void_p
isl.isl_ast_node_for_get_init.argtypes = [c_void_p]
isl.isl_ast_node_for_get_iterator.restype = c_void_p
isl.isl_ast_node_for_get_iterator.argtypes = [c_void_p]
isl.isl_ast_node_for_is_degenerate.argtypes = [c_void_p]
isl.isl_ast_node_copy.restype = c_void_p
isl.isl_ast_node_copy.argtypes = [c_void_p]
isl.isl_ast_node_free.restype = c_void_p
isl.isl_ast_node_free.argtypes = [c_void_p]
isl.isl_ast_node_to_str.restype = POINTER(c_char)
isl.isl_ast_node_to_str.argtypes = [c_void_p]

class ast_node_if(ast_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_node_if, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_node_if:
                arg0 = ast_node_if(arg0)
        except:
            raise
        ptr = isl.isl_ast_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_node_if("""%s""")' % s
        else:
            return 'isl.ast_node_if("%s")' % s
    def cond(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_if_get_cond(arg0.ptr)
        obj = ast_expr(ctx=ctx, ptr=res)
        return obj
    def get_cond(arg0):
        return arg0.cond()
    def else_node(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_if_get_else_node(arg0.ptr)
        obj = ast_node(ctx=ctx, ptr=res)
        return obj
    def get_else_node(arg0):
        return arg0.else_node()
    def then_node(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_if_get_then_node(arg0.ptr)
        obj = ast_node(ctx=ctx, ptr=res)
        return obj
    def get_then_node(arg0):
        return arg0.then_node()
    def has_else_node(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_if_has_else_node(arg0.ptr)
        if res < 0:
            raise
        return bool(res)

isl.isl_ast_node_if_get_cond.restype = c_void_p
isl.isl_ast_node_if_get_cond.argtypes = [c_void_p]
isl.isl_ast_node_if_get_else_node.restype = c_void_p
isl.isl_ast_node_if_get_else_node.argtypes = [c_void_p]
isl.isl_ast_node_if_get_then_node.restype = c_void_p
isl.isl_ast_node_if_get_then_node.argtypes = [c_void_p]
isl.isl_ast_node_if_has_else_node.argtypes = [c_void_p]
isl.isl_ast_node_copy.restype = c_void_p
isl.isl_ast_node_copy.argtypes = [c_void_p]
isl.isl_ast_node_free.restype = c_void_p
isl.isl_ast_node_free.argtypes = [c_void_p]
isl.isl_ast_node_to_str.restype = POINTER(c_char)
isl.isl_ast_node_to_str.argtypes = [c_void_p]

class ast_node_list(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is ast_node:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_ast_node_list_from_ast_node(isl.isl_ast_node_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == int:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_ast_node_list_alloc(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_node_list_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_node_list:
                arg0 = ast_node_list(arg0)
        except:
            raise
        ptr = isl.isl_ast_node_list_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_node_list("""%s""")' % s
        else:
            return 'isl.ast_node_list("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is ast_node_list:
                arg0 = ast_node_list(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is ast_node:
                arg1 = ast_node(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_list_add(isl.isl_ast_node_list_copy(arg0.ptr), isl.isl_ast_node_copy(arg1.ptr))
        obj = ast_node_list(ctx=ctx, ptr=res)
        return obj
    def concat(arg0, arg1):
        try:
            if not arg0.__class__ is ast_node_list:
                arg0 = ast_node_list(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is ast_node_list:
                arg1 = ast_node_list(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_list_concat(isl.isl_ast_node_list_copy(arg0.ptr), isl.isl_ast_node_list_copy(arg1.ptr))
        obj = ast_node_list(ctx=ctx, ptr=res)
        return obj
    def foreach(arg0, arg1):
        try:
            if not arg0.__class__ is ast_node_list:
                arg0 = ast_node_list(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = ast_node(ctx=arg0.ctx, ptr=(cb_arg0))
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_ast_node_list_foreach(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
    def at(arg0, arg1):
        try:
            if not arg0.__class__ is ast_node_list:
                arg0 = ast_node_list(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_list_get_at(arg0.ptr, arg1)
        obj = ast_node(ctx=ctx, ptr=res)
        return obj
    def get_at(arg0, arg1):
        return arg0.at(arg1)
    def size(arg0):
        try:
            if not arg0.__class__ is ast_node_list:
                arg0 = ast_node_list(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_list_size(arg0.ptr)
        if res < 0:
            raise
        return int(res)

isl.isl_ast_node_list_from_ast_node.restype = c_void_p
isl.isl_ast_node_list_from_ast_node.argtypes = [c_void_p]
isl.isl_ast_node_list_alloc.restype = c_void_p
isl.isl_ast_node_list_alloc.argtypes = [Context, c_int]
isl.isl_ast_node_list_add.restype = c_void_p
isl.isl_ast_node_list_add.argtypes = [c_void_p, c_void_p]
isl.isl_ast_node_list_concat.restype = c_void_p
isl.isl_ast_node_list_concat.argtypes = [c_void_p, c_void_p]
isl.isl_ast_node_list_foreach.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_ast_node_list_get_at.restype = c_void_p
isl.isl_ast_node_list_get_at.argtypes = [c_void_p, c_int]
isl.isl_ast_node_list_size.argtypes = [c_void_p]
isl.isl_ast_node_list_copy.restype = c_void_p
isl.isl_ast_node_list_copy.argtypes = [c_void_p]
isl.isl_ast_node_list_free.restype = c_void_p
isl.isl_ast_node_list_free.argtypes = [c_void_p]
isl.isl_ast_node_list_to_str.restype = POINTER(c_char)
isl.isl_ast_node_list_to_str.argtypes = [c_void_p]

class ast_node_mark(ast_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_node_mark, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_node_mark:
                arg0 = ast_node_mark(arg0)
        except:
            raise
        ptr = isl.isl_ast_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_node_mark("""%s""")' % s
        else:
            return 'isl.ast_node_mark("%s")' % s
    def id(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_mark_get_id(arg0.ptr)
        obj = id(ctx=ctx, ptr=res)
        return obj
    def get_id(arg0):
        return arg0.id()
    def node(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_mark_get_node(arg0.ptr)
        obj = ast_node(ctx=ctx, ptr=res)
        return obj
    def get_node(arg0):
        return arg0.node()

isl.isl_ast_node_mark_get_id.restype = c_void_p
isl.isl_ast_node_mark_get_id.argtypes = [c_void_p]
isl.isl_ast_node_mark_get_node.restype = c_void_p
isl.isl_ast_node_mark_get_node.argtypes = [c_void_p]
isl.isl_ast_node_copy.restype = c_void_p
isl.isl_ast_node_copy.argtypes = [c_void_p]
isl.isl_ast_node_free.restype = c_void_p
isl.isl_ast_node_free.argtypes = [c_void_p]
isl.isl_ast_node_to_str.restype = POINTER(c_char)
isl.isl_ast_node_to_str.argtypes = [c_void_p]

class ast_node_user(ast_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_ast_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(ast_node_user, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is ast_node_user:
                arg0 = ast_node_user(arg0)
        except:
            raise
        ptr = isl.isl_ast_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.ast_node_user("""%s""")' % s
        else:
            return 'isl.ast_node_user("%s")' % s
    def expr(arg0):
        try:
            if not arg0.__class__ is ast_node:
                arg0 = ast_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_ast_node_user_get_expr(arg0.ptr)
        obj = ast_expr(ctx=ctx, ptr=res)
        return obj
    def get_expr(arg0):
        return arg0.expr()

isl.isl_ast_node_user_get_expr.restype = c_void_p
isl.isl_ast_node_user_get_expr.argtypes = [c_void_p]
isl.isl_ast_node_copy.restype = c_void_p
isl.isl_ast_node_copy.argtypes = [c_void_p]
isl.isl_ast_node_free.restype = c_void_p
isl.isl_ast_node_free.argtypes = [c_void_p]
isl.isl_ast_node_to_str.restype = POINTER(c_char)
isl.isl_ast_node_to_str.argtypes = [c_void_p]

class union_map(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is basic_map:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_map_from_basic_map(isl.isl_basic_map_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is map:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_map_from_map(isl.isl_map_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_map_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_map_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ptr = isl.isl_union_map_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_map("""%s""")' % s
        else:
            return 'isl.union_map("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_affine_hull(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def apply_domain(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_apply_domain(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def apply_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_apply_range(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def coalesce(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_coalesce(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def compute_divs(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_compute_divs(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def deltas(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_deltas(isl.isl_union_map_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_detect_equalities(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def domain(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain(isl.isl_union_map_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def domain_factor_domain(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_factor_domain(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def domain_factor_range(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_factor_range(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def domain_map(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_map(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def domain_map_union_pw_multi_aff(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_map_union_pw_multi_aff(isl.isl_union_map_copy(arg0.ptr))
        obj = union_pw_multi_aff(ctx=ctx, ptr=res)
        return obj
    def domain_product(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_product(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def eq_at(arg0, arg1):
        if arg1.__class__ is multi_union_pw_aff:
            res = isl.isl_union_map_eq_at_multi_union_pw_aff(isl.isl_union_map_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = union_map(ctx=ctx, ptr=res)
            return obj
    def every_map(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = map(ctx=arg0.ctx, ptr=isl.isl_map_copy(cb_arg0))
            try:
                res = arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 1 if res else 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_union_map_every_map(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
        return bool(res)
    def factor_domain(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_factor_domain(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def factor_range(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_factor_range(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def fixed_power(arg0, arg1):
        if arg1.__class__ is val:
            res = isl.isl_union_map_fixed_power_val(isl.isl_union_map_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = union_map(ctx=ctx, ptr=res)
            return obj
    def foreach_map(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = map(ctx=arg0.ctx, ptr=(cb_arg0))
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_union_map_foreach_map(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
    @staticmethod
    def convert_from(arg0):
        if arg0.__class__ is union_pw_multi_aff:
            res = isl.isl_union_map_from_union_pw_multi_aff(isl.isl_union_pw_multi_aff_copy(arg0.ptr))
            ctx = arg0.ctx
            obj = union_map(ctx=ctx, ptr=res)
            return obj
        if arg0.__class__ is multi_union_pw_aff:
            res = isl.isl_union_map_from_multi_union_pw_aff(isl.isl_multi_union_pw_aff_copy(arg0.ptr))
            ctx = arg0.ctx
            obj = union_map(ctx=ctx, ptr=res)
            return obj
    @staticmethod
    def from_domain(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_from_domain(isl.isl_union_set_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    @staticmethod
    def from_domain_and_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_from_domain_and_range(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    @staticmethod
    def from_range(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_from_range(isl.isl_union_set_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_gist(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def gist_domain(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_gist_domain(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def gist_params(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_gist_params(isl.isl_union_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def gist_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_gist_range(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_intersect(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def intersect_domain(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_intersect_domain(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_intersect_params(isl.isl_union_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def intersect_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_intersect_range(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def is_bijective(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_bijective(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_empty(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_injective(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_injective(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_single_valued(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_single_valued(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_strict_subset(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_strict_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def isa_map(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_isa_map(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_lexmax(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def lexmin(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_lexmin(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def polyhedral_hull(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_polyhedral_hull(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_product(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def project_out_all_params(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_project_out_all_params(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def range(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range(isl.isl_union_map_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def range_factor_domain(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range_factor_domain(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def range_factor_range(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range_factor_range(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def range_map(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range_map(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range_product(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def reverse(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_reverse(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def subtract(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_subtract(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def subtract_domain(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_subtract_domain(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def subtract_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_subtract_range(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_union(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def wrap(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_wrap(isl.isl_union_map_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def zip(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_zip(isl.isl_union_map_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj

isl.isl_union_map_from_basic_map.restype = c_void_p
isl.isl_union_map_from_basic_map.argtypes = [c_void_p]
isl.isl_union_map_from_map.restype = c_void_p
isl.isl_union_map_from_map.argtypes = [c_void_p]
isl.isl_union_map_read_from_str.restype = c_void_p
isl.isl_union_map_read_from_str.argtypes = [Context, c_char_p]
isl.isl_union_map_affine_hull.restype = c_void_p
isl.isl_union_map_affine_hull.argtypes = [c_void_p]
isl.isl_union_map_apply_domain.restype = c_void_p
isl.isl_union_map_apply_domain.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_apply_range.restype = c_void_p
isl.isl_union_map_apply_range.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_coalesce.restype = c_void_p
isl.isl_union_map_coalesce.argtypes = [c_void_p]
isl.isl_union_map_compute_divs.restype = c_void_p
isl.isl_union_map_compute_divs.argtypes = [c_void_p]
isl.isl_union_map_deltas.restype = c_void_p
isl.isl_union_map_deltas.argtypes = [c_void_p]
isl.isl_union_map_detect_equalities.restype = c_void_p
isl.isl_union_map_detect_equalities.argtypes = [c_void_p]
isl.isl_union_map_domain.restype = c_void_p
isl.isl_union_map_domain.argtypes = [c_void_p]
isl.isl_union_map_domain_factor_domain.restype = c_void_p
isl.isl_union_map_domain_factor_domain.argtypes = [c_void_p]
isl.isl_union_map_domain_factor_range.restype = c_void_p
isl.isl_union_map_domain_factor_range.argtypes = [c_void_p]
isl.isl_union_map_domain_map.restype = c_void_p
isl.isl_union_map_domain_map.argtypes = [c_void_p]
isl.isl_union_map_domain_map_union_pw_multi_aff.restype = c_void_p
isl.isl_union_map_domain_map_union_pw_multi_aff.argtypes = [c_void_p]
isl.isl_union_map_domain_product.restype = c_void_p
isl.isl_union_map_domain_product.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_eq_at_multi_union_pw_aff.restype = c_void_p
isl.isl_union_map_eq_at_multi_union_pw_aff.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_every_map.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_union_map_factor_domain.restype = c_void_p
isl.isl_union_map_factor_domain.argtypes = [c_void_p]
isl.isl_union_map_factor_range.restype = c_void_p
isl.isl_union_map_factor_range.argtypes = [c_void_p]
isl.isl_union_map_fixed_power_val.restype = c_void_p
isl.isl_union_map_fixed_power_val.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_foreach_map.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_union_map_from_union_pw_multi_aff.restype = c_void_p
isl.isl_union_map_from_union_pw_multi_aff.argtypes = [c_void_p]
isl.isl_union_map_from_multi_union_pw_aff.restype = c_void_p
isl.isl_union_map_from_multi_union_pw_aff.argtypes = [c_void_p]
isl.isl_union_map_from_domain.restype = c_void_p
isl.isl_union_map_from_domain.argtypes = [c_void_p]
isl.isl_union_map_from_domain_and_range.restype = c_void_p
isl.isl_union_map_from_domain_and_range.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_from_range.restype = c_void_p
isl.isl_union_map_from_range.argtypes = [c_void_p]
isl.isl_union_map_gist.restype = c_void_p
isl.isl_union_map_gist.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_gist_domain.restype = c_void_p
isl.isl_union_map_gist_domain.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_gist_params.restype = c_void_p
isl.isl_union_map_gist_params.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_gist_range.restype = c_void_p
isl.isl_union_map_gist_range.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_intersect.restype = c_void_p
isl.isl_union_map_intersect.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_intersect_domain.restype = c_void_p
isl.isl_union_map_intersect_domain.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_intersect_params.restype = c_void_p
isl.isl_union_map_intersect_params.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_intersect_range.restype = c_void_p
isl.isl_union_map_intersect_range.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_is_bijective.argtypes = [c_void_p]
isl.isl_union_map_is_empty.argtypes = [c_void_p]
isl.isl_union_map_is_equal.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_is_injective.argtypes = [c_void_p]
isl.isl_union_map_is_single_valued.argtypes = [c_void_p]
isl.isl_union_map_is_strict_subset.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_is_subset.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_isa_map.argtypes = [c_void_p]
isl.isl_union_map_lexmax.restype = c_void_p
isl.isl_union_map_lexmax.argtypes = [c_void_p]
isl.isl_union_map_lexmin.restype = c_void_p
isl.isl_union_map_lexmin.argtypes = [c_void_p]
isl.isl_union_map_polyhedral_hull.restype = c_void_p
isl.isl_union_map_polyhedral_hull.argtypes = [c_void_p]
isl.isl_union_map_product.restype = c_void_p
isl.isl_union_map_product.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_project_out_all_params.restype = c_void_p
isl.isl_union_map_project_out_all_params.argtypes = [c_void_p]
isl.isl_union_map_range.restype = c_void_p
isl.isl_union_map_range.argtypes = [c_void_p]
isl.isl_union_map_range_factor_domain.restype = c_void_p
isl.isl_union_map_range_factor_domain.argtypes = [c_void_p]
isl.isl_union_map_range_factor_range.restype = c_void_p
isl.isl_union_map_range_factor_range.argtypes = [c_void_p]
isl.isl_union_map_range_map.restype = c_void_p
isl.isl_union_map_range_map.argtypes = [c_void_p]
isl.isl_union_map_range_product.restype = c_void_p
isl.isl_union_map_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_reverse.restype = c_void_p
isl.isl_union_map_reverse.argtypes = [c_void_p]
isl.isl_union_map_subtract.restype = c_void_p
isl.isl_union_map_subtract.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_subtract_domain.restype = c_void_p
isl.isl_union_map_subtract_domain.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_subtract_range.restype = c_void_p
isl.isl_union_map_subtract_range.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_union.restype = c_void_p
isl.isl_union_map_union.argtypes = [c_void_p, c_void_p]
isl.isl_union_map_wrap.restype = c_void_p
isl.isl_union_map_wrap.argtypes = [c_void_p]
isl.isl_union_map_zip.restype = c_void_p
isl.isl_union_map_zip.argtypes = [c_void_p]
isl.isl_union_map_copy.restype = c_void_p
isl.isl_union_map_copy.argtypes = [c_void_p]
isl.isl_union_map_free.restype = c_void_p
isl.isl_union_map_free.argtypes = [c_void_p]
isl.isl_union_map_to_str.restype = POINTER(c_char)
isl.isl_union_map_to_str.argtypes = [c_void_p]

class map(union_map):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_map_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        if len(args) == 1 and args[0].__class__ is basic_map:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_map_from_basic_map(isl.isl_basic_map_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_map_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ptr = isl.isl_map_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.map("""%s""")' % s
        else:
            return 'isl.map("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_affine_hull(isl.isl_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def apply_domain(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).apply_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_apply_domain(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def apply_range(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).apply_range(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_apply_range(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def coalesce(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_coalesce(isl.isl_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def complement(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_complement(isl.isl_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def deltas(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_deltas(isl.isl_map_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_detect_equalities(isl.isl_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def flatten(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_flatten(isl.isl_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def flatten_domain(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_flatten_domain(isl.isl_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def flatten_range(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_flatten_range(isl.isl_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def foreach_basic_map(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = basic_map(ctx=arg0.ctx, ptr=(cb_arg0))
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_map_foreach_basic_map(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).gist(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_gist(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def gist_domain(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_map(arg0).gist_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_gist_domain(isl.isl_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).intersect(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_intersect(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def intersect_domain(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_map(arg0).intersect_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_intersect_domain(isl.isl_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_map(arg0).intersect_params(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_intersect_params(isl.isl_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def intersect_range(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_map(arg0).intersect_range(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_intersect_range(isl.isl_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def is_bijective(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_is_bijective(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_disjoint(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).is_disjoint(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_is_disjoint(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_empty(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).is_equal(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_injective(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_is_injective(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_single_valued(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_is_single_valued(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_strict_subset(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).is_strict_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_is_strict_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).is_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_lexmax(isl.isl_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def lexmin(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_lexmin(isl.isl_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def polyhedral_hull(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_polyhedral_hull(isl.isl_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def reverse(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_reverse(isl.isl_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def sample(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_sample(isl.isl_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def subtract(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).subtract(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_subtract(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).union(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_union(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def unshifted_simple_hull(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_unshifted_simple_hull(isl.isl_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj

isl.isl_map_read_from_str.restype = c_void_p
isl.isl_map_read_from_str.argtypes = [Context, c_char_p]
isl.isl_map_from_basic_map.restype = c_void_p
isl.isl_map_from_basic_map.argtypes = [c_void_p]
isl.isl_map_affine_hull.restype = c_void_p
isl.isl_map_affine_hull.argtypes = [c_void_p]
isl.isl_map_apply_domain.restype = c_void_p
isl.isl_map_apply_domain.argtypes = [c_void_p, c_void_p]
isl.isl_map_apply_range.restype = c_void_p
isl.isl_map_apply_range.argtypes = [c_void_p, c_void_p]
isl.isl_map_coalesce.restype = c_void_p
isl.isl_map_coalesce.argtypes = [c_void_p]
isl.isl_map_complement.restype = c_void_p
isl.isl_map_complement.argtypes = [c_void_p]
isl.isl_map_deltas.restype = c_void_p
isl.isl_map_deltas.argtypes = [c_void_p]
isl.isl_map_detect_equalities.restype = c_void_p
isl.isl_map_detect_equalities.argtypes = [c_void_p]
isl.isl_map_flatten.restype = c_void_p
isl.isl_map_flatten.argtypes = [c_void_p]
isl.isl_map_flatten_domain.restype = c_void_p
isl.isl_map_flatten_domain.argtypes = [c_void_p]
isl.isl_map_flatten_range.restype = c_void_p
isl.isl_map_flatten_range.argtypes = [c_void_p]
isl.isl_map_foreach_basic_map.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_map_gist.restype = c_void_p
isl.isl_map_gist.argtypes = [c_void_p, c_void_p]
isl.isl_map_gist_domain.restype = c_void_p
isl.isl_map_gist_domain.argtypes = [c_void_p, c_void_p]
isl.isl_map_intersect.restype = c_void_p
isl.isl_map_intersect.argtypes = [c_void_p, c_void_p]
isl.isl_map_intersect_domain.restype = c_void_p
isl.isl_map_intersect_domain.argtypes = [c_void_p, c_void_p]
isl.isl_map_intersect_params.restype = c_void_p
isl.isl_map_intersect_params.argtypes = [c_void_p, c_void_p]
isl.isl_map_intersect_range.restype = c_void_p
isl.isl_map_intersect_range.argtypes = [c_void_p, c_void_p]
isl.isl_map_is_bijective.argtypes = [c_void_p]
isl.isl_map_is_disjoint.argtypes = [c_void_p, c_void_p]
isl.isl_map_is_empty.argtypes = [c_void_p]
isl.isl_map_is_equal.argtypes = [c_void_p, c_void_p]
isl.isl_map_is_injective.argtypes = [c_void_p]
isl.isl_map_is_single_valued.argtypes = [c_void_p]
isl.isl_map_is_strict_subset.argtypes = [c_void_p, c_void_p]
isl.isl_map_is_subset.argtypes = [c_void_p, c_void_p]
isl.isl_map_lexmax.restype = c_void_p
isl.isl_map_lexmax.argtypes = [c_void_p]
isl.isl_map_lexmin.restype = c_void_p
isl.isl_map_lexmin.argtypes = [c_void_p]
isl.isl_map_polyhedral_hull.restype = c_void_p
isl.isl_map_polyhedral_hull.argtypes = [c_void_p]
isl.isl_map_reverse.restype = c_void_p
isl.isl_map_reverse.argtypes = [c_void_p]
isl.isl_map_sample.restype = c_void_p
isl.isl_map_sample.argtypes = [c_void_p]
isl.isl_map_subtract.restype = c_void_p
isl.isl_map_subtract.argtypes = [c_void_p, c_void_p]
isl.isl_map_union.restype = c_void_p
isl.isl_map_union.argtypes = [c_void_p, c_void_p]
isl.isl_map_unshifted_simple_hull.restype = c_void_p
isl.isl_map_unshifted_simple_hull.argtypes = [c_void_p]
isl.isl_map_copy.restype = c_void_p
isl.isl_map_copy.argtypes = [c_void_p]
isl.isl_map_free.restype = c_void_p
isl.isl_map_free.argtypes = [c_void_p]
isl.isl_map_to_str.restype = POINTER(c_char)
isl.isl_map_to_str.argtypes = [c_void_p]

class basic_map(map):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_basic_map_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_basic_map_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ptr = isl.isl_basic_map_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.basic_map("""%s""")' % s
        else:
            return 'isl.basic_map("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_affine_hull(isl.isl_basic_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def apply_domain(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).apply_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_apply_domain(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def apply_range(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).apply_range(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_apply_range(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def deltas(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_deltas(isl.isl_basic_map_copy(arg0.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_detect_equalities(isl.isl_basic_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def flatten(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_flatten(isl.isl_basic_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def flatten_domain(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_flatten_domain(isl.isl_basic_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def flatten_range(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_flatten_range(isl.isl_basic_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).gist(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_gist(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).intersect(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_intersect(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def intersect_domain(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return map(arg0).intersect_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_intersect_domain(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def intersect_range(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return map(arg0).intersect_range(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_intersect_range(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def is_empty(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).is_equal(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).is_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_lexmax(isl.isl_basic_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def lexmin(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_lexmin(isl.isl_basic_map_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def reverse(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_reverse(isl.isl_basic_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def sample(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_sample(isl.isl_basic_map_copy(arg0.ptr))
        obj = basic_map(ctx=ctx, ptr=res)
        return obj
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).union(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_union(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj

isl.isl_basic_map_read_from_str.restype = c_void_p
isl.isl_basic_map_read_from_str.argtypes = [Context, c_char_p]
isl.isl_basic_map_affine_hull.restype = c_void_p
isl.isl_basic_map_affine_hull.argtypes = [c_void_p]
isl.isl_basic_map_apply_domain.restype = c_void_p
isl.isl_basic_map_apply_domain.argtypes = [c_void_p, c_void_p]
isl.isl_basic_map_apply_range.restype = c_void_p
isl.isl_basic_map_apply_range.argtypes = [c_void_p, c_void_p]
isl.isl_basic_map_deltas.restype = c_void_p
isl.isl_basic_map_deltas.argtypes = [c_void_p]
isl.isl_basic_map_detect_equalities.restype = c_void_p
isl.isl_basic_map_detect_equalities.argtypes = [c_void_p]
isl.isl_basic_map_flatten.restype = c_void_p
isl.isl_basic_map_flatten.argtypes = [c_void_p]
isl.isl_basic_map_flatten_domain.restype = c_void_p
isl.isl_basic_map_flatten_domain.argtypes = [c_void_p]
isl.isl_basic_map_flatten_range.restype = c_void_p
isl.isl_basic_map_flatten_range.argtypes = [c_void_p]
isl.isl_basic_map_gist.restype = c_void_p
isl.isl_basic_map_gist.argtypes = [c_void_p, c_void_p]
isl.isl_basic_map_intersect.restype = c_void_p
isl.isl_basic_map_intersect.argtypes = [c_void_p, c_void_p]
isl.isl_basic_map_intersect_domain.restype = c_void_p
isl.isl_basic_map_intersect_domain.argtypes = [c_void_p, c_void_p]
isl.isl_basic_map_intersect_range.restype = c_void_p
isl.isl_basic_map_intersect_range.argtypes = [c_void_p, c_void_p]
isl.isl_basic_map_is_empty.argtypes = [c_void_p]
isl.isl_basic_map_is_equal.argtypes = [c_void_p, c_void_p]
isl.isl_basic_map_is_subset.argtypes = [c_void_p, c_void_p]
isl.isl_basic_map_lexmax.restype = c_void_p
isl.isl_basic_map_lexmax.argtypes = [c_void_p]
isl.isl_basic_map_lexmin.restype = c_void_p
isl.isl_basic_map_lexmin.argtypes = [c_void_p]
isl.isl_basic_map_reverse.restype = c_void_p
isl.isl_basic_map_reverse.argtypes = [c_void_p]
isl.isl_basic_map_sample.restype = c_void_p
isl.isl_basic_map_sample.argtypes = [c_void_p]
isl.isl_basic_map_union.restype = c_void_p
isl.isl_basic_map_union.argtypes = [c_void_p, c_void_p]
isl.isl_basic_map_copy.restype = c_void_p
isl.isl_basic_map_copy.argtypes = [c_void_p]
isl.isl_basic_map_free.restype = c_void_p
isl.isl_basic_map_free.argtypes = [c_void_p]
isl.isl_basic_map_to_str.restype = POINTER(c_char)
isl.isl_basic_map_to_str.argtypes = [c_void_p]

class union_set(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is basic_set:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_from_basic_set(isl.isl_basic_set_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is set:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_from_set(isl.isl_set_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is point:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_from_point(isl.isl_point_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_set_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ptr = isl.isl_union_set_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_set("""%s""")' % s
        else:
            return 'isl.union_set("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_affine_hull(isl.isl_union_set_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def apply(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_apply(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def coalesce(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_coalesce(isl.isl_union_set_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def compute_divs(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_compute_divs(isl.isl_union_set_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_detect_equalities(isl.isl_union_set_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def every_set(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = set(ctx=arg0.ctx, ptr=isl.isl_set_copy(cb_arg0))
            try:
                res = arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 1 if res else 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_union_set_every_set(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
        return bool(res)
    def foreach_point(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = point(ctx=arg0.ctx, ptr=(cb_arg0))
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_union_set_foreach_point(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
    def foreach_set(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = set(ctx=arg0.ctx, ptr=(cb_arg0))
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_union_set_foreach_set(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_gist(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def gist_params(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_gist_params(isl.isl_union_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def identity(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_identity(isl.isl_union_set_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_intersect(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_intersect_params(isl.isl_union_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def is_empty(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_strict_subset(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_is_strict_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def isa_set(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_isa_set(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_lexmax(isl.isl_union_set_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def lexmin(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_lexmin(isl.isl_union_set_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def polyhedral_hull(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_polyhedral_hull(isl.isl_union_set_copy(arg0.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def preimage(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_union_set_preimage_multi_aff(isl.isl_union_set_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = union_set(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is pw_multi_aff:
            res = isl.isl_union_set_preimage_pw_multi_aff(isl.isl_union_set_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = union_set(ctx=ctx, ptr=res)
            return obj
        if arg1.__class__ is union_pw_multi_aff:
            res = isl.isl_union_set_preimage_union_pw_multi_aff(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = union_set(ctx=ctx, ptr=res)
            return obj
    def sample_point(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_sample_point(isl.isl_union_set_copy(arg0.ptr))
        obj = point(ctx=ctx, ptr=res)
        return obj
    def subtract(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_subtract(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_union(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def unwrap(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_unwrap(isl.isl_union_set_copy(arg0.ptr))
        obj = union_map(ctx=ctx, ptr=res)
        return obj

isl.isl_union_set_from_basic_set.restype = c_void_p
isl.isl_union_set_from_basic_set.argtypes = [c_void_p]
isl.isl_union_set_from_set.restype = c_void_p
isl.isl_union_set_from_set.argtypes = [c_void_p]
isl.isl_union_set_from_point.restype = c_void_p
isl.isl_union_set_from_point.argtypes = [c_void_p]
isl.isl_union_set_read_from_str.restype = c_void_p
isl.isl_union_set_read_from_str.argtypes = [Context, c_char_p]
isl.isl_union_set_affine_hull.restype = c_void_p
isl.isl_union_set_affine_hull.argtypes = [c_void_p]
isl.isl_union_set_apply.restype = c_void_p
isl.isl_union_set_apply.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_coalesce.restype = c_void_p
isl.isl_union_set_coalesce.argtypes = [c_void_p]
isl.isl_union_set_compute_divs.restype = c_void_p
isl.isl_union_set_compute_divs.argtypes = [c_void_p]
isl.isl_union_set_detect_equalities.restype = c_void_p
isl.isl_union_set_detect_equalities.argtypes = [c_void_p]
isl.isl_union_set_every_set.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_union_set_foreach_point.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_union_set_foreach_set.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_union_set_gist.restype = c_void_p
isl.isl_union_set_gist.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_gist_params.restype = c_void_p
isl.isl_union_set_gist_params.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_identity.restype = c_void_p
isl.isl_union_set_identity.argtypes = [c_void_p]
isl.isl_union_set_intersect.restype = c_void_p
isl.isl_union_set_intersect.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_intersect_params.restype = c_void_p
isl.isl_union_set_intersect_params.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_is_empty.argtypes = [c_void_p]
isl.isl_union_set_is_equal.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_is_strict_subset.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_is_subset.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_isa_set.argtypes = [c_void_p]
isl.isl_union_set_lexmax.restype = c_void_p
isl.isl_union_set_lexmax.argtypes = [c_void_p]
isl.isl_union_set_lexmin.restype = c_void_p
isl.isl_union_set_lexmin.argtypes = [c_void_p]
isl.isl_union_set_polyhedral_hull.restype = c_void_p
isl.isl_union_set_polyhedral_hull.argtypes = [c_void_p]
isl.isl_union_set_preimage_multi_aff.restype = c_void_p
isl.isl_union_set_preimage_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_preimage_pw_multi_aff.restype = c_void_p
isl.isl_union_set_preimage_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_preimage_union_pw_multi_aff.restype = c_void_p
isl.isl_union_set_preimage_union_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_sample_point.restype = c_void_p
isl.isl_union_set_sample_point.argtypes = [c_void_p]
isl.isl_union_set_subtract.restype = c_void_p
isl.isl_union_set_subtract.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_union.restype = c_void_p
isl.isl_union_set_union.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_unwrap.restype = c_void_p
isl.isl_union_set_unwrap.argtypes = [c_void_p]
isl.isl_union_set_copy.restype = c_void_p
isl.isl_union_set_copy.argtypes = [c_void_p]
isl.isl_union_set_free.restype = c_void_p
isl.isl_union_set_free.argtypes = [c_void_p]
isl.isl_union_set_to_str.restype = POINTER(c_char)
isl.isl_union_set_to_str.argtypes = [c_void_p]

class set(union_set):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_set_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        if len(args) == 1 and args[0].__class__ is basic_set:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_set_from_basic_set(isl.isl_basic_set_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is point:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_set_from_point(isl.isl_point_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_set_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ptr = isl.isl_set_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.set("""%s""")' % s
        else:
            return 'isl.set("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_affine_hull(isl.isl_set_copy(arg0.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def apply(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_set(arg0).apply(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_apply(isl.isl_set_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def coalesce(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_coalesce(isl.isl_set_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def complement(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_complement(isl.isl_set_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_detect_equalities(isl.isl_set_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def flatten(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_flatten(isl.isl_set_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def foreach_basic_set(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = basic_set(ctx=arg0.ctx, ptr=(cb_arg0))
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_set_foreach_basic_set(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
    def stride(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_get_stride(arg0.ptr, arg1)
        obj = val(ctx=ctx, ptr=res)
        return obj
    def get_stride(arg0, arg1):
        return arg0.stride(arg1)
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).gist(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_gist(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def identity(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_identity(isl.isl_set_copy(arg0.ptr))
        obj = map(ctx=ctx, ptr=res)
        return obj
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).intersect(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_intersect(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).intersect_params(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_intersect_params(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def is_disjoint(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).is_disjoint(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_is_disjoint(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_empty(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).is_equal(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_strict_subset(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).is_strict_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_is_strict_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).is_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_wrapping(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_is_wrapping(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_lexmax(isl.isl_set_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def lexmin(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_lexmin(isl.isl_set_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def max_val(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return union_set(arg0).max_val(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_max_val(arg0.ptr, arg1.ptr)
        obj = val(ctx=ctx, ptr=res)
        return obj
    def min_val(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return union_set(arg0).min_val(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_min_val(arg0.ptr, arg1.ptr)
        obj = val(ctx=ctx, ptr=res)
        return obj
    def polyhedral_hull(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_polyhedral_hull(isl.isl_set_copy(arg0.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def sample(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_sample(isl.isl_set_copy(arg0.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def sample_point(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_sample_point(isl.isl_set_copy(arg0.ptr))
        obj = point(ctx=ctx, ptr=res)
        return obj
    def subtract(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).subtract(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_subtract(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).union(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_union(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def unshifted_simple_hull(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_unshifted_simple_hull(isl.isl_set_copy(arg0.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj

isl.isl_set_read_from_str.restype = c_void_p
isl.isl_set_read_from_str.argtypes = [Context, c_char_p]
isl.isl_set_from_basic_set.restype = c_void_p
isl.isl_set_from_basic_set.argtypes = [c_void_p]
isl.isl_set_from_point.restype = c_void_p
isl.isl_set_from_point.argtypes = [c_void_p]
isl.isl_set_affine_hull.restype = c_void_p
isl.isl_set_affine_hull.argtypes = [c_void_p]
isl.isl_set_apply.restype = c_void_p
isl.isl_set_apply.argtypes = [c_void_p, c_void_p]
isl.isl_set_coalesce.restype = c_void_p
isl.isl_set_coalesce.argtypes = [c_void_p]
isl.isl_set_complement.restype = c_void_p
isl.isl_set_complement.argtypes = [c_void_p]
isl.isl_set_detect_equalities.restype = c_void_p
isl.isl_set_detect_equalities.argtypes = [c_void_p]
isl.isl_set_flatten.restype = c_void_p
isl.isl_set_flatten.argtypes = [c_void_p]
isl.isl_set_foreach_basic_set.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_set_get_stride.restype = c_void_p
isl.isl_set_get_stride.argtypes = [c_void_p, c_int]
isl.isl_set_gist.restype = c_void_p
isl.isl_set_gist.argtypes = [c_void_p, c_void_p]
isl.isl_set_identity.restype = c_void_p
isl.isl_set_identity.argtypes = [c_void_p]
isl.isl_set_intersect.restype = c_void_p
isl.isl_set_intersect.argtypes = [c_void_p, c_void_p]
isl.isl_set_intersect_params.restype = c_void_p
isl.isl_set_intersect_params.argtypes = [c_void_p, c_void_p]
isl.isl_set_is_disjoint.argtypes = [c_void_p, c_void_p]
isl.isl_set_is_empty.argtypes = [c_void_p]
isl.isl_set_is_equal.argtypes = [c_void_p, c_void_p]
isl.isl_set_is_strict_subset.argtypes = [c_void_p, c_void_p]
isl.isl_set_is_subset.argtypes = [c_void_p, c_void_p]
isl.isl_set_is_wrapping.argtypes = [c_void_p]
isl.isl_set_lexmax.restype = c_void_p
isl.isl_set_lexmax.argtypes = [c_void_p]
isl.isl_set_lexmin.restype = c_void_p
isl.isl_set_lexmin.argtypes = [c_void_p]
isl.isl_set_max_val.restype = c_void_p
isl.isl_set_max_val.argtypes = [c_void_p, c_void_p]
isl.isl_set_min_val.restype = c_void_p
isl.isl_set_min_val.argtypes = [c_void_p, c_void_p]
isl.isl_set_polyhedral_hull.restype = c_void_p
isl.isl_set_polyhedral_hull.argtypes = [c_void_p]
isl.isl_set_sample.restype = c_void_p
isl.isl_set_sample.argtypes = [c_void_p]
isl.isl_set_sample_point.restype = c_void_p
isl.isl_set_sample_point.argtypes = [c_void_p]
isl.isl_set_subtract.restype = c_void_p
isl.isl_set_subtract.argtypes = [c_void_p, c_void_p]
isl.isl_set_union.restype = c_void_p
isl.isl_set_union.argtypes = [c_void_p, c_void_p]
isl.isl_set_unshifted_simple_hull.restype = c_void_p
isl.isl_set_unshifted_simple_hull.argtypes = [c_void_p]
isl.isl_set_copy.restype = c_void_p
isl.isl_set_copy.argtypes = [c_void_p]
isl.isl_set_free.restype = c_void_p
isl.isl_set_free.argtypes = [c_void_p]
isl.isl_set_to_str.restype = POINTER(c_char)
isl.isl_set_to_str.argtypes = [c_void_p]

class basic_set(set):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_basic_set_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        if len(args) == 1 and args[0].__class__ is point:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_basic_set_from_point(isl.isl_point_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_basic_set_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ptr = isl.isl_basic_set_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.basic_set("""%s""")' % s
        else:
            return 'isl.basic_set("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_affine_hull(isl.isl_basic_set_copy(arg0.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def apply(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return set(arg0).apply(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_apply(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_detect_equalities(isl.isl_basic_set_copy(arg0.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def dim_max_val(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_dim_max_val(isl.isl_basic_set_copy(arg0.ptr), arg1)
        obj = val(ctx=ctx, ptr=res)
        return obj
    def flatten(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_flatten(isl.isl_basic_set_copy(arg0.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).gist(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_gist(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).intersect(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_intersect(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).intersect_params(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_intersect_params(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def is_empty(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).is_equal(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).is_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_wrapping(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_is_wrapping(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_lexmax(isl.isl_basic_set_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def lexmin(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_lexmin(isl.isl_basic_set_copy(arg0.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj
    def sample(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_sample(isl.isl_basic_set_copy(arg0.ptr))
        obj = basic_set(ctx=ctx, ptr=res)
        return obj
    def sample_point(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_sample_point(isl.isl_basic_set_copy(arg0.ptr))
        obj = point(ctx=ctx, ptr=res)
        return obj
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).union(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_union(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        obj = set(ctx=ctx, ptr=res)
        return obj

isl.isl_basic_set_read_from_str.restype = c_void_p
isl.isl_basic_set_read_from_str.argtypes = [Context, c_char_p]
isl.isl_basic_set_from_point.restype = c_void_p
isl.isl_basic_set_from_point.argtypes = [c_void_p]
isl.isl_basic_set_affine_hull.restype = c_void_p
isl.isl_basic_set_affine_hull.argtypes = [c_void_p]
isl.isl_basic_set_apply.restype = c_void_p
isl.isl_basic_set_apply.argtypes = [c_void_p, c_void_p]
isl.isl_basic_set_detect_equalities.restype = c_void_p
isl.isl_basic_set_detect_equalities.argtypes = [c_void_p]
isl.isl_basic_set_dim_max_val.restype = c_void_p
isl.isl_basic_set_dim_max_val.argtypes = [c_void_p, c_int]
isl.isl_basic_set_flatten.restype = c_void_p
isl.isl_basic_set_flatten.argtypes = [c_void_p]
isl.isl_basic_set_gist.restype = c_void_p
isl.isl_basic_set_gist.argtypes = [c_void_p, c_void_p]
isl.isl_basic_set_intersect.restype = c_void_p
isl.isl_basic_set_intersect.argtypes = [c_void_p, c_void_p]
isl.isl_basic_set_intersect_params.restype = c_void_p
isl.isl_basic_set_intersect_params.argtypes = [c_void_p, c_void_p]
isl.isl_basic_set_is_empty.argtypes = [c_void_p]
isl.isl_basic_set_is_equal.argtypes = [c_void_p, c_void_p]
isl.isl_basic_set_is_subset.argtypes = [c_void_p, c_void_p]
isl.isl_basic_set_is_wrapping.argtypes = [c_void_p]
isl.isl_basic_set_lexmax.restype = c_void_p
isl.isl_basic_set_lexmax.argtypes = [c_void_p]
isl.isl_basic_set_lexmin.restype = c_void_p
isl.isl_basic_set_lexmin.argtypes = [c_void_p]
isl.isl_basic_set_sample.restype = c_void_p
isl.isl_basic_set_sample.argtypes = [c_void_p]
isl.isl_basic_set_sample_point.restype = c_void_p
isl.isl_basic_set_sample_point.argtypes = [c_void_p]
isl.isl_basic_set_union.restype = c_void_p
isl.isl_basic_set_union.argtypes = [c_void_p, c_void_p]
isl.isl_basic_set_copy.restype = c_void_p
isl.isl_basic_set_copy.argtypes = [c_void_p]
isl.isl_basic_set_free.restype = c_void_p
isl.isl_basic_set_free.argtypes = [c_void_p]
isl.isl_basic_set_to_str.restype = POINTER(c_char)
isl.isl_basic_set_to_str.argtypes = [c_void_p]

class id(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_id_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_id_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is id:
                arg0 = id(arg0)
        except:
            raise
        ptr = isl.isl_id_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.id("""%s""")' % s
        else:
            return 'isl.id("%s")' % s
    def name(arg0):
        try:
            if not arg0.__class__ is id:
                arg0 = id(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_id_get_name(arg0.ptr)
        if res == 0:
            raise
        string = cast(res, c_char_p).value.decode('ascii')
        return string
    def get_name(arg0):
        return arg0.name()

isl.isl_id_read_from_str.restype = c_void_p
isl.isl_id_read_from_str.argtypes = [Context, c_char_p]
isl.isl_id_get_name.restype = POINTER(c_char)
isl.isl_id_get_name.argtypes = [c_void_p]
isl.isl_id_copy.restype = c_void_p
isl.isl_id_copy.argtypes = [c_void_p]
isl.isl_id_free.restype = c_void_p
isl.isl_id_free.argtypes = [c_void_p]
isl.isl_id_to_str.restype = POINTER(c_char)
isl.isl_id_to_str.argtypes = [c_void_p]

class multi_val(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_multi_val_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is multi_val:
                arg0 = multi_val(arg0)
        except:
            raise
        ptr = isl.isl_multi_val_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.multi_val("""%s""")' % s
        else:
            return 'isl.multi_val("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_val:
                arg0 = multi_val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_val_add(isl.isl_multi_val_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        obj = multi_val(ctx=ctx, ptr=res)
        return obj
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_val:
                arg0 = multi_val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_val_flat_range_product(isl.isl_multi_val_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        obj = multi_val(ctx=ctx, ptr=res)
        return obj
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_val:
                arg0 = multi_val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_val_product(isl.isl_multi_val_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        obj = multi_val(ctx=ctx, ptr=res)
        return obj
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_val:
                arg0 = multi_val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_val_range_product(isl.isl_multi_val_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        obj = multi_val(ctx=ctx, ptr=res)
        return obj

isl.isl_multi_val_add.restype = c_void_p
isl.isl_multi_val_add.argtypes = [c_void_p, c_void_p]
isl.isl_multi_val_flat_range_product.restype = c_void_p
isl.isl_multi_val_flat_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_val_product.restype = c_void_p
isl.isl_multi_val_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_val_range_product.restype = c_void_p
isl.isl_multi_val_range_product.argtypes = [c_void_p, c_void_p]
isl.isl_multi_val_copy.restype = c_void_p
isl.isl_multi_val_copy.argtypes = [c_void_p]
isl.isl_multi_val_free.restype = c_void_p
isl.isl_multi_val_free.argtypes = [c_void_p]
isl.isl_multi_val_to_str.restype = POINTER(c_char)
isl.isl_multi_val_to_str.argtypes = [c_void_p]

class point(basic_set):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_point_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is point:
                arg0 = point(arg0)
        except:
            raise
        ptr = isl.isl_point_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.point("""%s""")' % s
        else:
            return 'isl.point("%s")' % s

isl.isl_point_copy.restype = c_void_p
isl.isl_point_copy.argtypes = [c_void_p]
isl.isl_point_free.restype = c_void_p
isl.isl_point_free.argtypes = [c_void_p]
isl.isl_point_to_str.restype = POINTER(c_char)
isl.isl_point_to_str.argtypes = [c_void_p]

class schedule(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_schedule_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule:
                arg0 = schedule(arg0)
        except:
            raise
        ptr = isl.isl_schedule_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule("""%s""")' % s
        else:
            return 'isl.schedule("%s")' % s
    def map(arg0):
        try:
            if not arg0.__class__ is schedule:
                arg0 = schedule(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_get_map(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_map(arg0):
        return arg0.map()
    def root(arg0):
        try:
            if not arg0.__class__ is schedule:
                arg0 = schedule(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_get_root(arg0.ptr)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def get_root(arg0):
        return arg0.root()
    def pullback(arg0, arg1):
        if arg1.__class__ is union_pw_multi_aff:
            res = isl.isl_schedule_pullback_union_pw_multi_aff(isl.isl_schedule_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
            ctx = arg0.ctx
            obj = schedule(ctx=ctx, ptr=res)
            return obj

isl.isl_schedule_read_from_str.restype = c_void_p
isl.isl_schedule_read_from_str.argtypes = [Context, c_char_p]
isl.isl_schedule_get_map.restype = c_void_p
isl.isl_schedule_get_map.argtypes = [c_void_p]
isl.isl_schedule_get_root.restype = c_void_p
isl.isl_schedule_get_root.argtypes = [c_void_p]
isl.isl_schedule_pullback_union_pw_multi_aff.restype = c_void_p
isl.isl_schedule_pullback_union_pw_multi_aff.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_copy.restype = c_void_p
isl.isl_schedule_copy.argtypes = [c_void_p]
isl.isl_schedule_free.restype = c_void_p
isl.isl_schedule_free.argtypes = [c_void_p]
isl.isl_schedule_to_str.restype = POINTER(c_char)
isl.isl_schedule_to_str.argtypes = [c_void_p]

class schedule_constraints(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_schedule_constraints_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_constraints_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        ptr = isl.isl_schedule_constraints_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_constraints("""%s""")' % s
        else:
            return 'isl.schedule_constraints("%s")' % s
    def compute_schedule(arg0):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_compute_schedule(isl.isl_schedule_constraints_copy(arg0.ptr))
        obj = schedule(ctx=ctx, ptr=res)
        return obj
    def coincidence(arg0):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_get_coincidence(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_coincidence(arg0):
        return arg0.coincidence()
    def conditional_validity(arg0):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_get_conditional_validity(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_conditional_validity(arg0):
        return arg0.conditional_validity()
    def conditional_validity_condition(arg0):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_get_conditional_validity_condition(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_conditional_validity_condition(arg0):
        return arg0.conditional_validity_condition()
    def context(arg0):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_get_context(arg0.ptr)
        obj = set(ctx=ctx, ptr=res)
        return obj
    def get_context(arg0):
        return arg0.context()
    def domain(arg0):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_get_domain(arg0.ptr)
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def get_domain(arg0):
        return arg0.domain()
    def proximity(arg0):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_get_proximity(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_proximity(arg0):
        return arg0.proximity()
    def validity(arg0):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_get_validity(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_validity(arg0):
        return arg0.validity()
    @staticmethod
    def on_domain(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_on_domain(isl.isl_union_set_copy(arg0.ptr))
        obj = schedule_constraints(ctx=ctx, ptr=res)
        return obj
    def set_coincidence(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_set_coincidence(isl.isl_schedule_constraints_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = schedule_constraints(ctx=ctx, ptr=res)
        return obj
    def set_conditional_validity(arg0, arg1, arg2):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        try:
            if not arg2.__class__ is union_map:
                arg2 = union_map(arg2)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_set_conditional_validity(isl.isl_schedule_constraints_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr), isl.isl_union_map_copy(arg2.ptr))
        obj = schedule_constraints(ctx=ctx, ptr=res)
        return obj
    def set_context(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_set_context(isl.isl_schedule_constraints_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = schedule_constraints(ctx=ctx, ptr=res)
        return obj
    def set_proximity(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_set_proximity(isl.isl_schedule_constraints_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = schedule_constraints(ctx=ctx, ptr=res)
        return obj
    def set_validity(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_constraints:
                arg0 = schedule_constraints(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_constraints_set_validity(isl.isl_schedule_constraints_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = schedule_constraints(ctx=ctx, ptr=res)
        return obj

isl.isl_schedule_constraints_read_from_str.restype = c_void_p
isl.isl_schedule_constraints_read_from_str.argtypes = [Context, c_char_p]
isl.isl_schedule_constraints_compute_schedule.restype = c_void_p
isl.isl_schedule_constraints_compute_schedule.argtypes = [c_void_p]
isl.isl_schedule_constraints_get_coincidence.restype = c_void_p
isl.isl_schedule_constraints_get_coincidence.argtypes = [c_void_p]
isl.isl_schedule_constraints_get_conditional_validity.restype = c_void_p
isl.isl_schedule_constraints_get_conditional_validity.argtypes = [c_void_p]
isl.isl_schedule_constraints_get_conditional_validity_condition.restype = c_void_p
isl.isl_schedule_constraints_get_conditional_validity_condition.argtypes = [c_void_p]
isl.isl_schedule_constraints_get_context.restype = c_void_p
isl.isl_schedule_constraints_get_context.argtypes = [c_void_p]
isl.isl_schedule_constraints_get_domain.restype = c_void_p
isl.isl_schedule_constraints_get_domain.argtypes = [c_void_p]
isl.isl_schedule_constraints_get_proximity.restype = c_void_p
isl.isl_schedule_constraints_get_proximity.argtypes = [c_void_p]
isl.isl_schedule_constraints_get_validity.restype = c_void_p
isl.isl_schedule_constraints_get_validity.argtypes = [c_void_p]
isl.isl_schedule_constraints_on_domain.restype = c_void_p
isl.isl_schedule_constraints_on_domain.argtypes = [c_void_p]
isl.isl_schedule_constraints_set_coincidence.restype = c_void_p
isl.isl_schedule_constraints_set_coincidence.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_constraints_set_conditional_validity.restype = c_void_p
isl.isl_schedule_constraints_set_conditional_validity.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_schedule_constraints_set_context.restype = c_void_p
isl.isl_schedule_constraints_set_context.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_constraints_set_proximity.restype = c_void_p
isl.isl_schedule_constraints_set_proximity.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_constraints_set_validity.restype = c_void_p
isl.isl_schedule_constraints_set_validity.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_constraints_copy.restype = c_void_p
isl.isl_schedule_constraints_copy.argtypes = [c_void_p]
isl.isl_schedule_constraints_free.restype = c_void_p
isl.isl_schedule_constraints_free.argtypes = [c_void_p]
isl.isl_schedule_constraints_to_str.restype = POINTER(c_char)
isl.isl_schedule_constraints_to_str.argtypes = [c_void_p]

class schedule_node(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_band):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_context):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_domain):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_expansion):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_extension):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_filter):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_leaf):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_guard):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_mark):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_sequence):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        if len(args) == 1 and isinstance(args[0], schedule_node_set):
            self.ctx = args[0].ctx
            self.ptr = isl.isl_schedule_node_copy(args[0].ptr)
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        if "ptr" in keywords:
            type = isl.isl_schedule_node_get_type(keywords["ptr"])
            if type == 0:
                return schedule_node_band(**keywords)
            if type == 1:
                return schedule_node_context(**keywords)
            if type == 2:
                return schedule_node_domain(**keywords)
            if type == 3:
                return schedule_node_expansion(**keywords)
            if type == 4:
                return schedule_node_extension(**keywords)
            if type == 5:
                return schedule_node_filter(**keywords)
            if type == 6:
                return schedule_node_leaf(**keywords)
            if type == 7:
                return schedule_node_guard(**keywords)
            if type == 8:
                return schedule_node_mark(**keywords)
            if type == 9:
                return schedule_node_sequence(**keywords)
            if type == 10:
                return schedule_node_set(**keywords)
            raise
        return super(schedule_node, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node("""%s""")' % s
        else:
            return 'isl.schedule_node("%s")' % s
    def ancestor(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_ancestor(isl.isl_schedule_node_copy(arg0.ptr), arg1)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def child(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_child(isl.isl_schedule_node_copy(arg0.ptr), arg1)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def every_descendant(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = schedule_node(ctx=arg0.ctx, ptr=isl.isl_schedule_node_copy(cb_arg0))
            try:
                res = arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 1 if res else 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_schedule_node_every_descendant(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
        return bool(res)
    def first_child(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_first_child(isl.isl_schedule_node_copy(arg0.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def foreach_ancestor_top_down(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = schedule_node(ctx=arg0.ctx, ptr=isl.isl_schedule_node_copy(cb_arg0))
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_schedule_node_foreach_ancestor_top_down(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
    def foreach_descendant_top_down(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = schedule_node(ctx=arg0.ctx, ptr=isl.isl_schedule_node_copy(cb_arg0))
            try:
                res = arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 1 if res else 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_schedule_node_foreach_descendant_top_down(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
    @staticmethod
    def from_domain(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_from_domain(isl.isl_union_set_copy(arg0.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    @staticmethod
    def from_extension(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_from_extension(isl.isl_union_map_copy(arg0.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def ancestor_child_position(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is schedule_node:
                arg1 = schedule_node(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_ancestor_child_position(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return int(res)
    def get_ancestor_child_position(arg0, arg1):
        return arg0.ancestor_child_position(arg1)
    def child_position(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_child_position(arg0.ptr)
        if res < 0:
            raise
        return int(res)
    def get_child_position(arg0):
        return arg0.child_position()
    def prefix_schedule_multi_union_pw_aff(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_prefix_schedule_multi_union_pw_aff(arg0.ptr)
        obj = multi_union_pw_aff(ctx=ctx, ptr=res)
        return obj
    def get_prefix_schedule_multi_union_pw_aff(arg0):
        return arg0.prefix_schedule_multi_union_pw_aff()
    def prefix_schedule_union_map(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_prefix_schedule_union_map(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_prefix_schedule_union_map(arg0):
        return arg0.prefix_schedule_union_map()
    def prefix_schedule_union_pw_multi_aff(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_prefix_schedule_union_pw_multi_aff(arg0.ptr)
        obj = union_pw_multi_aff(ctx=ctx, ptr=res)
        return obj
    def get_prefix_schedule_union_pw_multi_aff(arg0):
        return arg0.prefix_schedule_union_pw_multi_aff()
    def schedule(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_schedule(arg0.ptr)
        obj = schedule(ctx=ctx, ptr=res)
        return obj
    def get_schedule(arg0):
        return arg0.schedule()
    def shared_ancestor(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is schedule_node:
                arg1 = schedule_node(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_shared_ancestor(arg0.ptr, arg1.ptr)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def get_shared_ancestor(arg0, arg1):
        return arg0.shared_ancestor(arg1)
    def tree_depth(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_tree_depth(arg0.ptr)
        if res < 0:
            raise
        return int(res)
    def get_tree_depth(arg0):
        return arg0.tree_depth()
    def graft_after(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is schedule_node:
                arg1 = schedule_node(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_graft_after(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_schedule_node_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def graft_before(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is schedule_node:
                arg1 = schedule_node(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_graft_before(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_schedule_node_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def has_children(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_has_children(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def has_next_sibling(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_has_next_sibling(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def has_parent(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_has_parent(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def has_previous_sibling(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_has_previous_sibling(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def insert_context(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_insert_context(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def insert_filter(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_insert_filter(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def insert_guard(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_insert_guard(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def insert_partial_schedule(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_insert_partial_schedule(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def insert_sequence(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set_list:
                arg1 = union_set_list(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_insert_sequence(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_union_set_list_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def insert_set(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set_list:
                arg1 = union_set_list(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_insert_set(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_union_set_list_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is schedule_node:
                arg1 = schedule_node(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subtree_anchored(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_is_subtree_anchored(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def map_descendant_bottom_up(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_void_p, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = schedule_node(ctx=arg0.ctx, ptr=(cb_arg0))
            try:
                res = arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return None
            return isl.isl_schedule_node_copy(res.ptr)
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_schedule_node_map_descendant_bottom_up(isl.isl_schedule_node_copy(arg0.ptr), cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def n_children(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_n_children(arg0.ptr)
        if res < 0:
            raise
        return int(res)
    def next_sibling(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_next_sibling(isl.isl_schedule_node_copy(arg0.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def order_after(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_order_after(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def order_before(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_order_before(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def parent(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_parent(isl.isl_schedule_node_copy(arg0.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def previous_sibling(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_previous_sibling(isl.isl_schedule_node_copy(arg0.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def root(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_root(isl.isl_schedule_node_copy(arg0.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj

isl.isl_schedule_node_ancestor.restype = c_void_p
isl.isl_schedule_node_ancestor.argtypes = [c_void_p, c_int]
isl.isl_schedule_node_child.restype = c_void_p
isl.isl_schedule_node_child.argtypes = [c_void_p, c_int]
isl.isl_schedule_node_every_descendant.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_schedule_node_first_child.restype = c_void_p
isl.isl_schedule_node_first_child.argtypes = [c_void_p]
isl.isl_schedule_node_foreach_ancestor_top_down.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_schedule_node_foreach_descendant_top_down.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_schedule_node_from_domain.restype = c_void_p
isl.isl_schedule_node_from_domain.argtypes = [c_void_p]
isl.isl_schedule_node_from_extension.restype = c_void_p
isl.isl_schedule_node_from_extension.argtypes = [c_void_p]
isl.isl_schedule_node_get_ancestor_child_position.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_get_child_position.argtypes = [c_void_p]
isl.isl_schedule_node_get_prefix_schedule_multi_union_pw_aff.restype = c_void_p
isl.isl_schedule_node_get_prefix_schedule_multi_union_pw_aff.argtypes = [c_void_p]
isl.isl_schedule_node_get_prefix_schedule_union_map.restype = c_void_p
isl.isl_schedule_node_get_prefix_schedule_union_map.argtypes = [c_void_p]
isl.isl_schedule_node_get_prefix_schedule_union_pw_multi_aff.restype = c_void_p
isl.isl_schedule_node_get_prefix_schedule_union_pw_multi_aff.argtypes = [c_void_p]
isl.isl_schedule_node_get_schedule.restype = c_void_p
isl.isl_schedule_node_get_schedule.argtypes = [c_void_p]
isl.isl_schedule_node_get_shared_ancestor.restype = c_void_p
isl.isl_schedule_node_get_shared_ancestor.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_get_tree_depth.argtypes = [c_void_p]
isl.isl_schedule_node_graft_after.restype = c_void_p
isl.isl_schedule_node_graft_after.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_graft_before.restype = c_void_p
isl.isl_schedule_node_graft_before.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_has_children.argtypes = [c_void_p]
isl.isl_schedule_node_has_next_sibling.argtypes = [c_void_p]
isl.isl_schedule_node_has_parent.argtypes = [c_void_p]
isl.isl_schedule_node_has_previous_sibling.argtypes = [c_void_p]
isl.isl_schedule_node_insert_context.restype = c_void_p
isl.isl_schedule_node_insert_context.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_insert_filter.restype = c_void_p
isl.isl_schedule_node_insert_filter.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_insert_guard.restype = c_void_p
isl.isl_schedule_node_insert_guard.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_insert_partial_schedule.restype = c_void_p
isl.isl_schedule_node_insert_partial_schedule.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_insert_sequence.restype = c_void_p
isl.isl_schedule_node_insert_sequence.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_insert_set.restype = c_void_p
isl.isl_schedule_node_insert_set.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_is_equal.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_is_subtree_anchored.argtypes = [c_void_p]
isl.isl_schedule_node_map_descendant_bottom_up.restype = c_void_p
isl.isl_schedule_node_map_descendant_bottom_up.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_schedule_node_n_children.argtypes = [c_void_p]
isl.isl_schedule_node_next_sibling.restype = c_void_p
isl.isl_schedule_node_next_sibling.argtypes = [c_void_p]
isl.isl_schedule_node_order_after.restype = c_void_p
isl.isl_schedule_node_order_after.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_order_before.restype = c_void_p
isl.isl_schedule_node_order_before.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_parent.restype = c_void_p
isl.isl_schedule_node_parent.argtypes = [c_void_p]
isl.isl_schedule_node_previous_sibling.restype = c_void_p
isl.isl_schedule_node_previous_sibling.argtypes = [c_void_p]
isl.isl_schedule_node_root.restype = c_void_p
isl.isl_schedule_node_root.argtypes = [c_void_p]
isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]
isl.isl_schedule_node_get_type.argtypes = [c_void_p]

class schedule_node_band(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_band, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_band:
                arg0 = schedule_node_band(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_band("""%s""")' % s
        else:
            return 'isl.schedule_node_band("%s")' % s
    def ast_build_options(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_get_ast_build_options(arg0.ptr)
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def get_ast_build_options(arg0):
        return arg0.ast_build_options()
    def ast_isolate_option(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_get_ast_isolate_option(arg0.ptr)
        obj = set(ctx=ctx, ptr=res)
        return obj
    def get_ast_isolate_option(arg0):
        return arg0.ast_isolate_option()
    def partial_schedule(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_get_partial_schedule(arg0.ptr)
        obj = multi_union_pw_aff(ctx=ctx, ptr=res)
        return obj
    def get_partial_schedule(arg0):
        return arg0.partial_schedule()
    def permutable(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_get_permutable(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def get_permutable(arg0):
        return arg0.permutable()
    def member_get_coincident(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_member_get_coincident(arg0.ptr, arg1)
        if res < 0:
            raise
        return bool(res)
    def member_set_coincident(arg0, arg1, arg2):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_member_set_coincident(isl.isl_schedule_node_copy(arg0.ptr), arg1, arg2)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def mod(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_mod(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def n_member(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_n_member(arg0.ptr)
        if res < 0:
            raise
        return int(res)
    def scale(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_scale(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def scale_down(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_scale_down(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def set_ast_build_options(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_set_ast_build_options(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def set_permutable(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_set_permutable(isl.isl_schedule_node_copy(arg0.ptr), arg1)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def shift(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_shift(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def split(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_split(isl.isl_schedule_node_copy(arg0.ptr), arg1)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def tile(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_tile(isl.isl_schedule_node_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def member_set_ast_loop_default(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_member_set_ast_loop_type(isl.isl_schedule_node_copy(arg0.ptr), arg1, 0)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def member_set_ast_loop_atomic(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_member_set_ast_loop_type(isl.isl_schedule_node_copy(arg0.ptr), arg1, 1)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def member_set_ast_loop_unroll(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_member_set_ast_loop_type(isl.isl_schedule_node_copy(arg0.ptr), arg1, 2)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj
    def member_set_ast_loop_separate(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_member_set_ast_loop_type(isl.isl_schedule_node_copy(arg0.ptr), arg1, 3)
        obj = schedule_node(ctx=ctx, ptr=res)
        return obj

isl.isl_schedule_node_band_get_ast_build_options.restype = c_void_p
isl.isl_schedule_node_band_get_ast_build_options.argtypes = [c_void_p]
isl.isl_schedule_node_band_get_ast_isolate_option.restype = c_void_p
isl.isl_schedule_node_band_get_ast_isolate_option.argtypes = [c_void_p]
isl.isl_schedule_node_band_get_partial_schedule.restype = c_void_p
isl.isl_schedule_node_band_get_partial_schedule.argtypes = [c_void_p]
isl.isl_schedule_node_band_get_permutable.argtypes = [c_void_p]
isl.isl_schedule_node_band_member_get_coincident.argtypes = [c_void_p, c_int]
isl.isl_schedule_node_band_member_set_coincident.restype = c_void_p
isl.isl_schedule_node_band_member_set_coincident.argtypes = [c_void_p, c_int, c_int]
isl.isl_schedule_node_band_mod.restype = c_void_p
isl.isl_schedule_node_band_mod.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_band_n_member.argtypes = [c_void_p]
isl.isl_schedule_node_band_scale.restype = c_void_p
isl.isl_schedule_node_band_scale.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_band_scale_down.restype = c_void_p
isl.isl_schedule_node_band_scale_down.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_band_set_ast_build_options.restype = c_void_p
isl.isl_schedule_node_band_set_ast_build_options.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_band_set_permutable.restype = c_void_p
isl.isl_schedule_node_band_set_permutable.argtypes = [c_void_p, c_int]
isl.isl_schedule_node_band_shift.restype = c_void_p
isl.isl_schedule_node_band_shift.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_band_split.restype = c_void_p
isl.isl_schedule_node_band_split.argtypes = [c_void_p, c_int]
isl.isl_schedule_node_band_tile.restype = c_void_p
isl.isl_schedule_node_band_tile.argtypes = [c_void_p, c_void_p]
isl.isl_schedule_node_band_member_set_ast_loop_type.restype = c_void_p
isl.isl_schedule_node_band_member_set_ast_loop_type.argtypes = [c_void_p, c_int, c_int]
isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_context(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_context, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_context:
                arg0 = schedule_node_context(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_context("""%s""")' % s
        else:
            return 'isl.schedule_node_context("%s")' % s
    def context(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_context_get_context(arg0.ptr)
        obj = set(ctx=ctx, ptr=res)
        return obj
    def get_context(arg0):
        return arg0.context()

isl.isl_schedule_node_context_get_context.restype = c_void_p
isl.isl_schedule_node_context_get_context.argtypes = [c_void_p]
isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_domain(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_domain, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_domain:
                arg0 = schedule_node_domain(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_domain("""%s""")' % s
        else:
            return 'isl.schedule_node_domain("%s")' % s
    def domain(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_domain_get_domain(arg0.ptr)
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def get_domain(arg0):
        return arg0.domain()

isl.isl_schedule_node_domain_get_domain.restype = c_void_p
isl.isl_schedule_node_domain_get_domain.argtypes = [c_void_p]
isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_expansion(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_expansion, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_expansion:
                arg0 = schedule_node_expansion(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_expansion("""%s""")' % s
        else:
            return 'isl.schedule_node_expansion("%s")' % s
    def contraction(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_expansion_get_contraction(arg0.ptr)
        obj = union_pw_multi_aff(ctx=ctx, ptr=res)
        return obj
    def get_contraction(arg0):
        return arg0.contraction()
    def expansion(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_expansion_get_expansion(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_expansion(arg0):
        return arg0.expansion()

isl.isl_schedule_node_expansion_get_contraction.restype = c_void_p
isl.isl_schedule_node_expansion_get_contraction.argtypes = [c_void_p]
isl.isl_schedule_node_expansion_get_expansion.restype = c_void_p
isl.isl_schedule_node_expansion_get_expansion.argtypes = [c_void_p]
isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_extension(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_extension, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_extension:
                arg0 = schedule_node_extension(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_extension("""%s""")' % s
        else:
            return 'isl.schedule_node_extension("%s")' % s
    def extension(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_extension_get_extension(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_extension(arg0):
        return arg0.extension()

isl.isl_schedule_node_extension_get_extension.restype = c_void_p
isl.isl_schedule_node_extension_get_extension.argtypes = [c_void_p]
isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_filter(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_filter, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_filter:
                arg0 = schedule_node_filter(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_filter("""%s""")' % s
        else:
            return 'isl.schedule_node_filter("%s")' % s
    def filter(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_filter_get_filter(arg0.ptr)
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def get_filter(arg0):
        return arg0.filter()

isl.isl_schedule_node_filter_get_filter.restype = c_void_p
isl.isl_schedule_node_filter_get_filter.argtypes = [c_void_p]
isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_guard(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_guard, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_guard:
                arg0 = schedule_node_guard(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_guard("""%s""")' % s
        else:
            return 'isl.schedule_node_guard("%s")' % s
    def guard(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_guard_get_guard(arg0.ptr)
        obj = set(ctx=ctx, ptr=res)
        return obj
    def get_guard(arg0):
        return arg0.guard()

isl.isl_schedule_node_guard_get_guard.restype = c_void_p
isl.isl_schedule_node_guard_get_guard.argtypes = [c_void_p]
isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_leaf(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_leaf, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_leaf:
                arg0 = schedule_node_leaf(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_leaf("""%s""")' % s
        else:
            return 'isl.schedule_node_leaf("%s")' % s

isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_mark(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_mark, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_mark:
                arg0 = schedule_node_mark(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_mark("""%s""")' % s
        else:
            return 'isl.schedule_node_mark("%s")' % s

isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_sequence(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_sequence, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_sequence:
                arg0 = schedule_node_sequence(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_sequence("""%s""")' % s
        else:
            return 'isl.schedule_node_sequence("%s")' % s

isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class schedule_node_set(schedule_node):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __new__(cls, *args, **keywords):
        return super(schedule_node_set, cls).__new__(cls)
    def __str__(arg0):
        try:
            if not arg0.__class__ is schedule_node_set:
                arg0 = schedule_node_set(arg0)
        except:
            raise
        ptr = isl.isl_schedule_node_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node_set("""%s""")' % s
        else:
            return 'isl.schedule_node_set("%s")' % s

isl.isl_schedule_node_copy.restype = c_void_p
isl.isl_schedule_node_copy.argtypes = [c_void_p]
isl.isl_schedule_node_free.restype = c_void_p
isl.isl_schedule_node_free.argtypes = [c_void_p]
isl.isl_schedule_node_to_str.restype = POINTER(c_char)
isl.isl_schedule_node_to_str.argtypes = [c_void_p]

class union_access_info(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is union_map:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_access_info_from_sink(isl.isl_union_map_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_access_info_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        ptr = isl.isl_union_access_info_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_access_info("""%s""")' % s
        else:
            return 'isl.union_access_info("%s")' % s
    def compute_flow(arg0):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_compute_flow(isl.isl_union_access_info_copy(arg0.ptr))
        obj = union_flow(ctx=ctx, ptr=res)
        return obj
    def set_kill(arg0, arg1):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_set_kill(isl.isl_union_access_info_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_access_info(ctx=ctx, ptr=res)
        return obj
    def set_may_source(arg0, arg1):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_set_may_source(isl.isl_union_access_info_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_access_info(ctx=ctx, ptr=res)
        return obj
    def set_must_source(arg0, arg1):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_set_must_source(isl.isl_union_access_info_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_access_info(ctx=ctx, ptr=res)
        return obj
    def set_schedule(arg0, arg1):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is schedule:
                arg1 = schedule(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_set_schedule(isl.isl_union_access_info_copy(arg0.ptr), isl.isl_schedule_copy(arg1.ptr))
        obj = union_access_info(ctx=ctx, ptr=res)
        return obj
    def set_schedule_map(arg0, arg1):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_set_schedule_map(isl.isl_union_access_info_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        obj = union_access_info(ctx=ctx, ptr=res)
        return obj

isl.isl_union_access_info_from_sink.restype = c_void_p
isl.isl_union_access_info_from_sink.argtypes = [c_void_p]
isl.isl_union_access_info_compute_flow.restype = c_void_p
isl.isl_union_access_info_compute_flow.argtypes = [c_void_p]
isl.isl_union_access_info_set_kill.restype = c_void_p
isl.isl_union_access_info_set_kill.argtypes = [c_void_p, c_void_p]
isl.isl_union_access_info_set_may_source.restype = c_void_p
isl.isl_union_access_info_set_may_source.argtypes = [c_void_p, c_void_p]
isl.isl_union_access_info_set_must_source.restype = c_void_p
isl.isl_union_access_info_set_must_source.argtypes = [c_void_p, c_void_p]
isl.isl_union_access_info_set_schedule.restype = c_void_p
isl.isl_union_access_info_set_schedule.argtypes = [c_void_p, c_void_p]
isl.isl_union_access_info_set_schedule_map.restype = c_void_p
isl.isl_union_access_info_set_schedule_map.argtypes = [c_void_p, c_void_p]
isl.isl_union_access_info_copy.restype = c_void_p
isl.isl_union_access_info_copy.argtypes = [c_void_p]
isl.isl_union_access_info_free.restype = c_void_p
isl.isl_union_access_info_free.argtypes = [c_void_p]
isl.isl_union_access_info_to_str.restype = POINTER(c_char)
isl.isl_union_access_info_to_str.argtypes = [c_void_p]

class union_flow(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_flow_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ptr = isl.isl_union_flow_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_flow("""%s""")' % s
        else:
            return 'isl.union_flow("%s")' % s
    def full_may_dependence(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_full_may_dependence(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_full_may_dependence(arg0):
        return arg0.full_may_dependence()
    def full_must_dependence(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_full_must_dependence(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_full_must_dependence(arg0):
        return arg0.full_must_dependence()
    def may_dependence(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_may_dependence(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_may_dependence(arg0):
        return arg0.may_dependence()
    def may_no_source(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_may_no_source(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_may_no_source(arg0):
        return arg0.may_no_source()
    def must_dependence(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_must_dependence(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_must_dependence(arg0):
        return arg0.must_dependence()
    def must_no_source(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_must_no_source(arg0.ptr)
        obj = union_map(ctx=ctx, ptr=res)
        return obj
    def get_must_no_source(arg0):
        return arg0.must_no_source()

isl.isl_union_flow_get_full_may_dependence.restype = c_void_p
isl.isl_union_flow_get_full_may_dependence.argtypes = [c_void_p]
isl.isl_union_flow_get_full_must_dependence.restype = c_void_p
isl.isl_union_flow_get_full_must_dependence.argtypes = [c_void_p]
isl.isl_union_flow_get_may_dependence.restype = c_void_p
isl.isl_union_flow_get_may_dependence.argtypes = [c_void_p]
isl.isl_union_flow_get_may_no_source.restype = c_void_p
isl.isl_union_flow_get_may_no_source.argtypes = [c_void_p]
isl.isl_union_flow_get_must_dependence.restype = c_void_p
isl.isl_union_flow_get_must_dependence.argtypes = [c_void_p]
isl.isl_union_flow_get_must_no_source.restype = c_void_p
isl.isl_union_flow_get_must_no_source.argtypes = [c_void_p]
isl.isl_union_flow_copy.restype = c_void_p
isl.isl_union_flow_copy.argtypes = [c_void_p]
isl.isl_union_flow_free.restype = c_void_p
isl.isl_union_flow_free.argtypes = [c_void_p]
isl.isl_union_flow_to_str.restype = POINTER(c_char)
isl.isl_union_flow_to_str.argtypes = [c_void_p]

class union_set_list(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is union_set:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_list_from_union_set(isl.isl_union_set_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == int:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_list_alloc(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_set_list_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is union_set_list:
                arg0 = union_set_list(arg0)
        except:
            raise
        ptr = isl.isl_union_set_list_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_set_list("""%s""")' % s
        else:
            return 'isl.union_set_list("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is union_set_list:
                arg0 = union_set_list(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_list_add(isl.isl_union_set_list_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        obj = union_set_list(ctx=ctx, ptr=res)
        return obj
    def concat(arg0, arg1):
        try:
            if not arg0.__class__ is union_set_list:
                arg0 = union_set_list(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set_list:
                arg1 = union_set_list(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_list_concat(isl.isl_union_set_list_copy(arg0.ptr), isl.isl_union_set_list_copy(arg1.ptr))
        obj = union_set_list(ctx=ctx, ptr=res)
        return obj
    def foreach(arg0, arg1):
        try:
            if not arg0.__class__ is union_set_list:
                arg0 = union_set_list(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = union_set(ctx=arg0.ctx, ptr=(cb_arg0))
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_union_set_list_foreach(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise (exc_info[0][0], exc_info[0][1], exc_info[0][2])
        if res < 0:
            raise
    def at(arg0, arg1):
        try:
            if not arg0.__class__ is union_set_list:
                arg0 = union_set_list(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_list_get_at(arg0.ptr, arg1)
        obj = union_set(ctx=ctx, ptr=res)
        return obj
    def get_at(arg0, arg1):
        return arg0.at(arg1)
    def size(arg0):
        try:
            if not arg0.__class__ is union_set_list:
                arg0 = union_set_list(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_list_size(arg0.ptr)
        if res < 0:
            raise
        return int(res)

isl.isl_union_set_list_from_union_set.restype = c_void_p
isl.isl_union_set_list_from_union_set.argtypes = [c_void_p]
isl.isl_union_set_list_alloc.restype = c_void_p
isl.isl_union_set_list_alloc.argtypes = [Context, c_int]
isl.isl_union_set_list_add.restype = c_void_p
isl.isl_union_set_list_add.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_list_concat.restype = c_void_p
isl.isl_union_set_list_concat.argtypes = [c_void_p, c_void_p]
isl.isl_union_set_list_foreach.argtypes = [c_void_p, c_void_p, c_void_p]
isl.isl_union_set_list_get_at.restype = c_void_p
isl.isl_union_set_list_get_at.argtypes = [c_void_p, c_int]
isl.isl_union_set_list_size.argtypes = [c_void_p]
isl.isl_union_set_list_copy.restype = c_void_p
isl.isl_union_set_list_copy.argtypes = [c_void_p]
isl.isl_union_set_list_free.restype = c_void_p
isl.isl_union_set_list_free.argtypes = [c_void_p]
isl.isl_union_set_list_to_str.restype = POINTER(c_char)
isl.isl_union_set_list_to_str.argtypes = [c_void_p]

class val(object):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == int:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_val_int_from_si(self.ctx, args[0])
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_val_read_from_str(self.ctx, args[0].encode('ascii'))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_val_free(self.ptr)
    def __str__(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ptr = isl.isl_val_to_str(arg0.ptr)
        res = cast(ptr, c_char_p).value.decode('ascii')
        libc.free(ptr)
        return res
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.val("""%s""")' % s
        else:
            return 'isl.val("%s")' % s
    def abs(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_abs(isl.isl_val_copy(arg0.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def abs_eq(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_abs_eq(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_add(isl.isl_val_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def ceil(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_ceil(isl.isl_val_copy(arg0.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def cmp_si(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_cmp_si(arg0.ptr, arg1)
        return res
    def div(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_div(isl.isl_val_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def eq(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_eq(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def floor(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_floor(isl.isl_val_copy(arg0.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def gcd(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_gcd(isl.isl_val_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def ge(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_ge(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def gt(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_gt(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    @staticmethod
    def infty():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_infty(ctx)
        obj = val(ctx=ctx, ptr=res)
        return obj
    def inv(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_inv(isl.isl_val_copy(arg0.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def is_divisible_by(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_divisible_by(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_infty(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_infty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_int(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_int(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_nan(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_nan(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_neg(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_neg(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_neginfty(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_neginfty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_negone(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_negone(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_nonneg(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_nonneg(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_nonpos(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_nonpos(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_one(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_one(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_pos(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_pos(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_rat(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_rat(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_zero(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_is_zero(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def le(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_le(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def lt(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_lt(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def max(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_max(isl.isl_val_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def min(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_min(isl.isl_val_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def mod(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_mod(isl.isl_val_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def mul(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_mul(isl.isl_val_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    @staticmethod
    def nan():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_nan(ctx)
        obj = val(ctx=ctx, ptr=res)
        return obj
    def ne(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_ne(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def neg(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_neg(isl.isl_val_copy(arg0.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    @staticmethod
    def neginfty():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_neginfty(ctx)
        obj = val(ctx=ctx, ptr=res)
        return obj
    @staticmethod
    def negone():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_negone(ctx)
        obj = val(ctx=ctx, ptr=res)
        return obj
    @staticmethod
    def one():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_one(ctx)
        obj = val(ctx=ctx, ptr=res)
        return obj
    def pow2(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_pow2(isl.isl_val_copy(arg0.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def sgn(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_sgn(arg0.ptr)
        return res
    def sub(arg0, arg1):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is val:
                arg1 = val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_sub(isl.isl_val_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    def trunc(arg0):
        try:
            if not arg0.__class__ is val:
                arg0 = val(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_val_trunc(isl.isl_val_copy(arg0.ptr))
        obj = val(ctx=ctx, ptr=res)
        return obj
    @staticmethod
    def zero():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_zero(ctx)
        obj = val(ctx=ctx, ptr=res)
        return obj

isl.isl_val_int_from_si.restype = c_void_p
isl.isl_val_int_from_si.argtypes = [Context, c_long]
isl.isl_val_read_from_str.restype = c_void_p
isl.isl_val_read_from_str.argtypes = [Context, c_char_p]
isl.isl_val_abs.restype = c_void_p
isl.isl_val_abs.argtypes = [c_void_p]
isl.isl_val_abs_eq.argtypes = [c_void_p, c_void_p]
isl.isl_val_add.restype = c_void_p
isl.isl_val_add.argtypes = [c_void_p, c_void_p]
isl.isl_val_ceil.restype = c_void_p
isl.isl_val_ceil.argtypes = [c_void_p]
isl.isl_val_cmp_si.argtypes = [c_void_p, c_long]
isl.isl_val_div.restype = c_void_p
isl.isl_val_div.argtypes = [c_void_p, c_void_p]
isl.isl_val_eq.argtypes = [c_void_p, c_void_p]
isl.isl_val_floor.restype = c_void_p
isl.isl_val_floor.argtypes = [c_void_p]
isl.isl_val_gcd.restype = c_void_p
isl.isl_val_gcd.argtypes = [c_void_p, c_void_p]
isl.isl_val_ge.argtypes = [c_void_p, c_void_p]
isl.isl_val_gt.argtypes = [c_void_p, c_void_p]
isl.isl_val_infty.restype = c_void_p
isl.isl_val_infty.argtypes = [Context]
isl.isl_val_inv.restype = c_void_p
isl.isl_val_inv.argtypes = [c_void_p]
isl.isl_val_is_divisible_by.argtypes = [c_void_p, c_void_p]
isl.isl_val_is_infty.argtypes = [c_void_p]
isl.isl_val_is_int.argtypes = [c_void_p]
isl.isl_val_is_nan.argtypes = [c_void_p]
isl.isl_val_is_neg.argtypes = [c_void_p]
isl.isl_val_is_neginfty.argtypes = [c_void_p]
isl.isl_val_is_negone.argtypes = [c_void_p]
isl.isl_val_is_nonneg.argtypes = [c_void_p]
isl.isl_val_is_nonpos.argtypes = [c_void_p]
isl.isl_val_is_one.argtypes = [c_void_p]
isl.isl_val_is_pos.argtypes = [c_void_p]
isl.isl_val_is_rat.argtypes = [c_void_p]
isl.isl_val_is_zero.argtypes = [c_void_p]
isl.isl_val_le.argtypes = [c_void_p, c_void_p]
isl.isl_val_lt.argtypes = [c_void_p, c_void_p]
isl.isl_val_max.restype = c_void_p
isl.isl_val_max.argtypes = [c_void_p, c_void_p]
isl.isl_val_min.restype = c_void_p
isl.isl_val_min.argtypes = [c_void_p, c_void_p]
isl.isl_val_mod.restype = c_void_p
isl.isl_val_mod.argtypes = [c_void_p, c_void_p]
isl.isl_val_mul.restype = c_void_p
isl.isl_val_mul.argtypes = [c_void_p, c_void_p]
isl.isl_val_nan.restype = c_void_p
isl.isl_val_nan.argtypes = [Context]
isl.isl_val_ne.argtypes = [c_void_p, c_void_p]
isl.isl_val_neg.restype = c_void_p
isl.isl_val_neg.argtypes = [c_void_p]
isl.isl_val_neginfty.restype = c_void_p
isl.isl_val_neginfty.argtypes = [Context]
isl.isl_val_negone.restype = c_void_p
isl.isl_val_negone.argtypes = [Context]
isl.isl_val_one.restype = c_void_p
isl.isl_val_one.argtypes = [Context]
isl.isl_val_pow2.restype = c_void_p
isl.isl_val_pow2.argtypes = [c_void_p]
isl.isl_val_sgn.argtypes = [c_void_p]
isl.isl_val_sub.restype = c_void_p
isl.isl_val_sub.argtypes = [c_void_p, c_void_p]
isl.isl_val_trunc.restype = c_void_p
isl.isl_val_trunc.argtypes = [c_void_p]
isl.isl_val_zero.restype = c_void_p
isl.isl_val_zero.argtypes = [Context]
isl.isl_val_copy.restype = c_void_p
isl.isl_val_copy.argtypes = [c_void_p]
isl.isl_val_free.restype = c_void_p
isl.isl_val_free.argtypes = [c_void_p]
isl.isl_val_to_str.restype = POINTER(c_char)
isl.isl_val_to_str.argtypes = [c_void_p]
