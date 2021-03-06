/*  This file is part of Misli.

    Misli is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Misli is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Misli.  If not, see <http://www.gnu.org/licenses/>.
*/

#ifndef CANVAS_H
#define CANVAS_H

#include <QWidget>
#include <QMouseEvent>
#include <QLineEdit>
#include <QMenu>
#include <QLabel>
#include <QPushButton>

#include "misli_desktop/misliwindow.h"
#include "misli_desktop/mislidesktopgui.h"
#include "misli_desktop/editnotedialogue.h"

class CanvasWidget : public QWidget
{
    Q_OBJECT

public:
    //Functions
    CanvasWidget(MisliWindow *misliWindow_, NoteFile *nf);
    ~CanvasWidget();

    Note *getNoteUnderMouse(int mouseX , int mouseY);
    Note *getNoteClickedForResize(int mouseX , int mouseY);
    Link *getLinkUnderMouse(int x,int y); //returns one link (not necesserily the top one) under the mouse
    Link *getControlPointUnderMouse(int x, int y);

    void unproject(double screenX, double screenY, double &realX, double &realY);
    void project(double realX, double realY, double &screenX, double &screenY);
    QPointF unproject(QPointF);
    QLineF project(QLineF);
    QRectF project(QRectF);
    QPointF project(QPointF);
    double projectX(double realX);
    double projectY(double realY);
    double unprojectX(double screenX);
    double unprojectY(double screenY);
    double heightScaleFactor();
    QPointF mousePos();

    void centerEyeOnNote(Note * nt);
    void updateCursorPosition();

    bool mimeDataIsCompatible(const QMimeData *mimeData);
    void pasteMimeData(const QMimeData *mimeData);

    //Properties
    NoteFile *noteFile();
    Library *library(){
        return misliWindow->misliDesktopGUI->misliLibrary;
    }

    //Variables
    MisliWindow *misliWindow;
    Note *cpChangeNote;
    Link *linkOnControlPointDrag;

    QMenu *contextMenu, detailsMenu, per_tag_filter_menu;
    QLabel *infoLabel;
    QTimer *move_func_timeout;
    QTime lastReleaseEvent;

//    Library * currentDir_m=nullptr;
    NoteFile *currentNoteFile = nullptr, *lastNoteFile = nullptr;
    QMetaObject::Connection nfChangedConnecton;

    double distanceToPrimeNoteX, distanceToPrimeNoteY, resizeX, resizeY;
    int XonPush, YonPush, PushLeft;
    double EyeXOnPush, EyeYOnPush;
    bool timedOutMove, moveOn, noteResizeOn, userIsDraggingStuff, draggedStuffIsValid, linkControlPointDragOn;
    bool linkingIsOn;
    bool ctrlUpdateHack;

signals:
    void linkingStateToggled(bool);

public slots:
    //Properties
    void setNoteFile(NoteFile* newNoteFile);
//    void setCurrentDir(Library * newDir);

    //Other
    void startMove();
    QString copySelectedNotes(NoteFile *sourceNotefile, NoteFile *targetNoteFile);
    void paste();
    void jumpToNearestNote();
    void doubleClick();
    void handleMousePress(Qt::MouseButton button);
    void handleMouseRelease(Qt::MouseButton button);

protected:
    void paintEvent(QPaintEvent *);
    void mousePressEvent(QMouseEvent *event){
        handleMousePress(event->button());
    }
    void mouseReleaseEvent(QMouseEvent *event){
        handleMouseRelease(event->button());
    }
    void mouseDoubleClickEvent(QMouseEvent *);
    void wheelEvent(QWheelEvent *event);
    void mouseMoveEvent(QMouseEvent *event);
    void dragEnterEvent(QDragEnterEvent *event);
    void dragLeaveEvent(QDragLeaveEvent *);
    void dropEvent(QDropEvent *event);

private:
    QMetaObject::Connection visualChangeConnection;
};

#endif // CANVAS_H
