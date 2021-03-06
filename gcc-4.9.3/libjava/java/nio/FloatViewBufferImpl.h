
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __java_nio_FloatViewBufferImpl__
#define __java_nio_FloatViewBufferImpl__

#pragma interface

#include <java/nio/FloatBuffer.h>
extern "Java"
{
  namespace java
  {
    namespace nio
    {
        class ByteBuffer;
        class ByteOrder;
        class FloatBuffer;
        class FloatViewBufferImpl;
    }
  }
}

class java::nio::FloatViewBufferImpl : public ::java::nio::FloatBuffer
{

public: // actually package-private
  FloatViewBufferImpl(::java::nio::ByteBuffer *, jint);
public:
  FloatViewBufferImpl(::java::nio::ByteBuffer *, jint, jint, jint, jint, jint, jboolean, ::java::nio::ByteOrder *);
  jfloat get();
  jfloat get(jint);
  ::java::nio::FloatBuffer * put(jfloat);
  ::java::nio::FloatBuffer * put(jint, jfloat);
  ::java::nio::FloatBuffer * compact();
  ::java::nio::FloatBuffer * slice();
public: // actually package-private
  ::java::nio::FloatBuffer * duplicate(jboolean);
public:
  ::java::nio::FloatBuffer * duplicate();
  ::java::nio::FloatBuffer * asReadOnlyBuffer();
  jboolean isReadOnly();
  jboolean isDirect();
  ::java::nio::ByteOrder * order();
private:
  jint __attribute__((aligned(__alignof__( ::java::nio::FloatBuffer)))) offset;
  ::java::nio::ByteBuffer * bb;
  jboolean readOnly;
  ::java::nio::ByteOrder * endian;
public:
  static ::java::lang::Class class$;
};

#endif // __java_nio_FloatViewBufferImpl__
