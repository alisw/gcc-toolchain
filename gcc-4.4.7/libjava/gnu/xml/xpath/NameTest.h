
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __gnu_xml_xpath_NameTest__
#define __gnu_xml_xpath_NameTest__

#pragma interface

#include <gnu/xml/xpath/Test.h>
extern "Java"
{
  namespace gnu
  {
    namespace xml
    {
      namespace xpath
      {
          class NameTest;
          class Test;
      }
    }
  }
  namespace javax
  {
    namespace xml
    {
      namespace namespace
      {
          class QName;
      }
    }
  }
  namespace org
  {
    namespace w3c
    {
      namespace dom
      {
          class Node;
      }
    }
  }
}

class gnu::xml::xpath::NameTest : public ::gnu::xml::xpath::Test
{

public:
  NameTest(::javax::xml::namespace::QName *, jboolean, jboolean);
  jboolean matchesAny();
  jboolean matchesAnyLocalName();
  jboolean matches(::org::w3c::dom::Node *, jint, jint);
public: // actually package-private
  static ::java::lang::String * getLocalName(::org::w3c::dom::Node *);
  static jboolean equal(::java::lang::String *, ::java::lang::String *);
public:
  ::gnu::xml::xpath::Test * clone(::java::lang::Object *);
  jboolean references(::javax::xml::namespace::QName *);
  ::java::lang::String * toString();
public: // actually package-private
  ::javax::xml::namespace::QName * __attribute__((aligned(__alignof__( ::gnu::xml::xpath::Test)))) qName;
  jboolean anyLocalName;
  jboolean any;
public:
  static ::java::lang::Class class$;
};

#endif // __gnu_xml_xpath_NameTest__
