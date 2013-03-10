/* This program is licensed under GNU GPL . For the full notice see the
 * license.txt file or google the full text of the GPL*/

#ifndef GLWIDGET_H
#define GLWIDGET_H

#include <QGLWidget>

#include "common.h"
#include "../../petko10.h"

#include "editnotedialogue.h"
#include "note.h"
#include "notefile.h"
#include "link.h"

class MisliWindow;

class GLWidget : public QGLWidget
{
    Q_OBJECT

public:

    //Functions
    GLWidget(MisliWindow *msl_w_);
    ~GLWidget();

    QSize sizeHint() const;
    void setupViewport(int,int);

    Note *get_note_under_mouse(int x , int y);
    Note *get_note_clicked_for_resize(int x , int y);
    Link *get_link_under_mouse(int x,int y); //returns one link (not necesserily the top one) onder the mouse

    int unproject_to_plane(float z,float x_on_scr,float y_on_scr,float &x,float &y); //runs gluUnproject for point[x_on_scr,y_on_scr] on the plane (parallel to x->,y-> ) in depth z
    int unproject_to_plane(float z,float x_on_scr,float y_on_scr,double &x,double &y);
    int project_from_plane(double x_on_plane,double y_on_plane,double z_plane,double &x,double &y,double &z);

    void initGLenv();
    void setupGLenv();

    MisliInstance *misl_i();
    NotesVector *curr_note();

    void set_eye_coords_from_curr_nf();
    void save_eye_coords_to_nf();

    //Variables
    GLdouble modelview[16];
    GLdouble projection[16];
    GLint viewport[4];
    QFont font;

    MisliWindow *msl_w;

    Eye eye;
    Note *mouse_note;

    float move_x, move_y, resize_x, resize_y;
    int XonPush,YonPush,PushLeft,current_mouse_x,current_mouse_y;
    float EyeXOnPush,EyeYOnPush;
    bool ctrl_is_pressed,shift_is_pressed;
    bool timed_out_move,move_on,resize_on;

public slots:
    void move_func();
    void set_linking_on();
    void set_linking_off();
    int copy();
    int paste();
    int cut();

protected:
    void initializeGL();
    void paintGL();
    void resizeGL(int width, int height);
    void mousePressEvent(QMouseEvent *event);
    void mouseReleaseEvent(QMouseEvent *event);
    void mouseDoubleClickEvent(QMouseEvent *);
    void wheelEvent(QWheelEvent *event);
    void mouseMoveEvent(QMouseEvent *event);

private:
    QTimer *move_func_timeout;

};

#endif //GLWIDGET_H
