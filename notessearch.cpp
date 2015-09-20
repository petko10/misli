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

#include <algorithm>

#include "notessearch.h"

NotesSearch::NotesSearch()
{
}

int NotesSearch::loadNotes(MisliInstance *misliInstance, float initial_probability)
{
    int notes_loaded=0;

    for(MisliDir* misliDir: misliInstance->misliDirs()  ){
        notes_loaded += loadNotes(misliDir,initial_probability);
    }
    return notes_loaded;
}
int NotesSearch::loadNotes(MisliDir *misliDir, float initial_probability)
{
    int notes_loaded=0;
    SearchItem searchItem;

    //Clear all items from this MisliDir if there are any
    QMutableListIterator<SearchItem> searchItemIterator(searchItems);
    while(searchItemIterator.hasNext()){
        searchItem = searchItemIterator.next();
        if(searchItem.md==misliDir) searchItemIterator.remove();
    }

    for(auto nf: misliDir->noteFiles()){
        notes_loaded += loadNotes(nf, misliDir, initial_probability);
    }
    return notes_loaded;
}
int NotesSearch::loadNotes(NoteFile *noteFile, MisliDir* misliDir, float initial_probability)
{
    int notes_loaded=0;
    SearchItem searchItem;

    //Clear all items from this NF if there are any
    QMutableListIterator<SearchItem> searchItemIterator(searchItems);
    while(searchItemIterator.hasNext()){
        searchItem = searchItemIterator.next();
        if(searchItem.nf==noteFile) searchItemIterator.remove();
    }

    //(Re)load all items
    for(Note *nt: noteFile->notes){
        //if(nt->type!=NoteType::textFile){ //don't search through the text files (too large)
        searchItem.nt=nt;
        searchItem.probability=initial_probability;
        searchItem.nf = noteFile;
        searchItem.md = misliDir;
        searchItems.push_back(searchItem);
        notes_loaded++;
        //}
    }
    return notes_loaded;
}

int NotesSearch::rowCount(const QModelIndex &) const
{
    if(searchResults.size()<200){
        return searchResults.size();
    }else return 200;

}
QVariant NotesSearch::data(const QModelIndex & index, int role) const
{
    if(role==Qt::DisplayRole) return searchResults.at(index.row()).text;
    return QVariant();
}
void NotesSearch::findByText(QString searchString)
{
    int oldSearchResultsSize = searchResults.size();
    searchResults.clear();

    //Skip everything if there's no search string
    if(!searchString.isEmpty()){
        searchResults = searchItems;
    }

    bool addPrecedingDots, addTrailingDots; //when shortening the text - where shortened add dots

    QMutableListIterator<SearchItem> searchResultsIterator(searchResults);
    while(searchResultsIterator.hasNext()){
        SearchItem &currentItem = searchResultsIterator.next();

        //Full match in the beginning (no capitals)
        if(currentItem.nt->text().startsWith(searchString, Qt::CaseInsensitive)){
            currentItem.probability = currentItem.probability*1; //100% (just for readability)
            //Get only the first 100 characters
            currentItem.text = currentItem.nt->text_m.left(100);
            if(currentItem.text.size()==100){
                addTrailingDots = true;
            }else{
                addTrailingDots = false;
            }
            addPrecedingDots = false;

        }else if(currentItem.nt->text().contains(searchString, Qt::CaseInsensitive)){
            //Full match somewhere else (no capitals)
            currentItem.probability = currentItem.probability*0.9; //90%
            //Get the string with 50 preceding characters and 50 after
            int index = currentItem.nt->text().indexOf(searchString, Qt::CaseInsensitive);
            if( index<50 ){
                index = 0;
                addPrecedingDots = false;
            }else{
                index -= 50;
                addPrecedingDots = true;
            }

            currentItem.text = currentItem.nt->text_m.mid(index,index+searchString.size()+100);

            if(currentItem.text.size()>=(index+searchString.size()+100)){
                addTrailingDots = true;
            }else{
                addTrailingDots = false;
            }
        }else//Other types of matches
            //if(){}
        {
            searchResultsIterator.remove();
            addPrecedingDots = false;
            addTrailingDots = false;
        }

        if(addPrecedingDots){
            currentItem.text.prepend("...");
        }
        if(addTrailingDots){
            currentItem.text.append("...");
        }
    }

    std::sort(searchResults.begin(),searchResults.end(),compareItems); //order by probability

    emit dataChanged(index(0,0),index(oldSearchResultsSize-1,0)); //all of the data has changed
}

bool NotesSearch::compareItems(SearchItem first, SearchItem second)
{
    return first.probability>second.probability;
}