
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __gnu_classpath_jdwp_event_filters_ClassOnlyFilter__
#define __gnu_classpath_jdwp_event_filters_ClassOnlyFilter__

#pragma interface

#include <java/lang/Object.h>
extern "Java"
{
  namespace gnu
  {
    namespace classpath
    {
      namespace jdwp
      {
        namespace event
        {
            class Event;
          namespace filters
          {
              class ClassOnlyFilter;
          }
        }
        namespace id
        {
            class ReferenceTypeId;
        }
      }
    }
  }
}

class gnu::classpath::jdwp::event::filters::ClassOnlyFilter : public ::java::lang::Object
{

public:
  ClassOnlyFilter(::gnu::classpath::jdwp::id::ReferenceTypeId *);
  virtual ::gnu::classpath::jdwp::id::ReferenceTypeId * getType();
  virtual jboolean matches(::gnu::classpath::jdwp::event::Event *);
private:
  ::gnu::classpath::jdwp::id::ReferenceTypeId * __attribute__((aligned(__alignof__( ::java::lang::Object)))) _id;
public:
  static ::java::lang::Class class$;
};

#endif // __gnu_classpath_jdwp_event_filters_ClassOnlyFilter__
