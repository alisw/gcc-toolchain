
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __javax_swing_plaf_basic_BasicListUI__
#define __javax_swing_plaf_basic_BasicListUI__

#pragma interface

#include <javax/swing/plaf/ListUI.h>
#include <gcj/array.h>

extern "Java"
{
  namespace java
  {
    namespace awt
    {
        class Dimension;
        class Graphics;
        class Point;
        class Rectangle;
      namespace event
      {
          class FocusListener;
      }
    }
    namespace beans
    {
        class PropertyChangeListener;
    }
  }
  namespace javax
  {
    namespace swing
    {
        class CellRendererPane;
        class JComponent;
        class JList;
        class ListCellRenderer;
        class ListModel;
        class ListSelectionModel;
      namespace event
      {
          class ListDataListener;
          class ListSelectionListener;
          class MouseInputListener;
      }
      namespace plaf
      {
          class ComponentUI;
        namespace basic
        {
            class BasicListUI;
            class BasicListUI$ListAction;
        }
      }
    }
  }
}

class javax::swing::plaf::basic::BasicListUI : public ::javax::swing::plaf::ListUI
{

public:
  static ::javax::swing::plaf::ComponentUI * createUI(::javax::swing::JComponent *);
public: // actually protected
  virtual jint getRowHeight(jint);
public:
  virtual ::java::awt::Rectangle * getCellBounds(::javax::swing::JList *, jint, jint);
private:
  jint getCellHeight(jint);
public: // actually protected
  virtual jint convertRowToY(jint);
  virtual jint convertYToRow(jint);
  virtual void updateLayoutState();
  virtual void maybeUpdateLayoutState();
public:
  BasicListUI();
public: // actually protected
  virtual void installDefaults();
  virtual void uninstallDefaults();
  virtual void installListeners();
  virtual void uninstallListeners();
  virtual void installKeyboardActions();
  virtual void uninstallKeyboardActions();
public:
  virtual void installUI(::javax::swing::JComponent *);
  virtual void uninstallUI(::javax::swing::JComponent *);
  virtual ::java::awt::Dimension * getPreferredSize(::javax::swing::JComponent *);
public: // actually protected
  virtual void paintCell(::java::awt::Graphics *, jint, ::java::awt::Rectangle *, ::javax::swing::ListCellRenderer *, ::javax::swing::ListModel *, ::javax::swing::ListSelectionModel *, jint);
public:
  virtual void paint(::java::awt::Graphics *, ::javax::swing::JComponent *);
  virtual jint locationToIndex(::javax::swing::JList *, ::java::awt::Point *);
  virtual ::java::awt::Point * indexToLocation(::javax::swing::JList *, jint);
public: // actually protected
  virtual ::java::awt::event::FocusListener * createFocusListener();
  virtual ::javax::swing::event::ListDataListener * createListDataListener();
  virtual ::javax::swing::event::ListSelectionListener * createListSelectionListener();
  virtual ::javax::swing::event::MouseInputListener * createMouseInputListener();
  virtual ::java::beans::PropertyChangeListener * createPropertyChangeListener();
  virtual void selectNextIndex();
  virtual void selectPreviousIndex();
  static const jint modelChanged = 1;
  static const jint selectionModelChanged = 2;
  static const jint fontChanged = 4;
  static const jint fixedCellWidthChanged = 8;
  static const jint fixedCellHeightChanged = 16;
  static const jint prototypeCellValueChanged = 32;
  static const jint cellRendererChanged = 64;
  ::java::awt::event::FocusListener * __attribute__((aligned(__alignof__( ::javax::swing::plaf::ListUI)))) focusListener;
  ::javax::swing::event::ListDataListener * listDataListener;
  ::javax::swing::event::ListSelectionListener * listSelectionListener;
  ::javax::swing::event::MouseInputListener * mouseInputListener;
  ::java::beans::PropertyChangeListener * propertyChangeListener;
  ::javax::swing::JList * list;
  jint cellHeight;
  jint cellWidth;
  JArray< jint > * cellHeights;
  jint updateLayoutStateNeeded;
  ::javax::swing::CellRendererPane * rendererPane;
public: // actually package-private
  ::javax::swing::plaf::basic::BasicListUI$ListAction * action;
public:
  static ::java::lang::Class class$;
};

#endif // __javax_swing_plaf_basic_BasicListUI__