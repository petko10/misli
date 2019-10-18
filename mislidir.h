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

#ifndef MISLIDIR_H
#define MISLIDIR_H

#include <QTimer>
#include <QSettings>
#include <QFileSystemWatcher>

#include "util.h"
#include "util.h"

#include "notefile.h"
#include "common.h"

class MisliInstance;
class Canvas;

class MisliDir : public QObject

{
    Q_OBJECT

public:
    //Functions
    MisliDir(QString nts_dir, bool enableFSWatch = true);
    ~MisliDir();

    int makeNotesFile(QString);
    void unloadAllNoteFiles();
    void deleteAllNoteFiles();

    NoteFile * noteFileByName(QString name);
    NoteFile * defaultNfOnStartup();

    //Properties
    float defaultEyeZ();
    QList<NoteFile*> noteFiles();

    //Variables
    QList<NoteFile*> noteFiles_m; //all the notefiles
    QFileSystemWatcher *fs_watch; //to watch the dir for changes
    QTimer * hangingNfCheck; //periodical check for unaccounted for note files
    QString folderPath;
    QSettings settings;
    bool keepHistoryViaGit = false;

    bool debug,fsWatchIsEnabled;

signals:
    //Property chabges
    void defaultEyeZChanged(float);
    void noteFilesChanged();

public slots:
    //Set properties
    void setDefaultEyeZ(float);

    //Other
    void loadNoteFile(QString pathToNoteFile);
    void loadNoteFiles();
    void reinitNotesPointingToNotefiles();

    void checkForHangingNFs();
    void handleChangedFile(QString filePath);

    void handleSaveRequest(NoteFile *nf);
    void softDeleteNF(NoteFile *nf);

};

#endif // MISLIDIR_H
