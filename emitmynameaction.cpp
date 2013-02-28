#include "emitmynameaction.h"

EmitMyNameAction::EmitMyNameAction(QString name_,QMenu *qmenu_):
    QAction(qmenu_)
{
    setCheckable(1);
    qmenu=qmenu_;
    name=name_;
    setText(name);
    connect(this,SIGNAL(triggered()),this,SLOT(emit_triggered_with_name()));
}

void EmitMyNameAction::emit_triggered_with_name()
{
    check_only_me();
    emit triggered_with_name(name);
}

void EmitMyNameAction::check_only_me()
{
    for(int i=0;i<qmenu->actions().size();i++){
        qmenu->actions().at(i)->setChecked(0);
    }
    setChecked(1);
}