
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __gnu_gcj_runtime_PersistentByteMap$ByteWrapper__
#define __gnu_gcj_runtime_PersistentByteMap$ByteWrapper__

#pragma interface

#include <java/lang/Object.h>
#include <gcj/array.h>

extern "Java"
{
  namespace gnu
  {
    namespace gcj
    {
      namespace runtime
      {
          class PersistentByteMap;
          class PersistentByteMap$ByteWrapper;
      }
    }
  }
}

class gnu::gcj::runtime::PersistentByteMap$ByteWrapper : public ::java::lang::Object
{

public:
  PersistentByteMap$ByteWrapper(::gnu::gcj::runtime::PersistentByteMap *, JArray< jbyte > *);
  jint hashCode();
  jboolean equals(::java::lang::Object *);
public: // actually package-private
  JArray< jbyte > * __attribute__((aligned(__alignof__( ::java::lang::Object)))) bytes;
  jint hash;
  ::gnu::gcj::runtime::PersistentByteMap * this$0;
public:
  static ::java::lang::Class class$;
};

#endif // __gnu_gcj_runtime_PersistentByteMap$ByteWrapper__
