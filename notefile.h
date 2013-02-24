/* This program is licensed under GNU GPL . For the full notice see the
 * license.txt file or google the full text of the GPL*/

#ifndef NOTEFILE_H
#define NOTEFILE_H

#include "note.h"
#include <string>

class MisliInstance;

class NoteFile { // all notes and supporting elements (info) for a note file

public:
    //Variables
    int id; //reserved ids: -1=clipboard nf
    char *name;
    NotesVector *note;
    int last_note_id;
    std::vector<std::string> comment; //komentarite vyv file-a
    std::vector<int> free_id; //komentarite vyv file-a
    char *full_file_addr;
    MisliInstance *misl_i;
    double eye_x,eye_y,eye_z;
    std::vector<std::string> *nf_z; //history of the notefile
    bool is_displayed_first_on_startup;

    //Functions
    NoteFile();
    //NoteFile(MisliInstance *m_i,const char *ime, int idd);
    Note *get_first_selected_note();
    Note *get_lowest_id_note();
    Note *get_note_by_id(int id);
    void clear_note_selection();
    void clear_link_selection();
    void make_coords_relative_to(double x,double y);
    int get_new_id();

    Note *add_note_base(MisliInstance *m_i,const char *text,double x,double y,double z,double a,double b,double font_size,QDate dt_made,QDate dt_mod);
    Note *add_note(MisliInstance *m_i,int id,const char *text,double x,double y,double z,double a,double b,double font_size,QDate dt_made,QDate dt_mod);
    Note *add_note(MisliInstance *m_i,const char *text,double x,double y,double z,double a,double b,double font_size,QDate dt_made,QDate dt_mod);
    Note *add_note(Note* nt);

    int delete_note(Note *);
    int delete_note(unsigned int);
    int delete_selected();

    int init(MisliInstance*,const char*,const char*);
    int init(NoteFile* nf);
    int init_links();
    int init_notes();
    int save();
    void set_to_current();
    void find_free_ids();

    //File parser
    //new_vaule()
    //read_value(int i);

};

#endif // NOTEFILE_H