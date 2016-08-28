from mingus.containers import Note
from mingus.containers.note_container import NoteContainer
from mingus.midi import fluidsynth

fluidsynth.init("GeneralUser.sf2")
fluidsynth.play_NoteContainer(NoteContainer(["C", "E"]))
note = Note("C-5")
# note.
# fluidsynth.play_Note(note)
fluidsynth.play_Note(64,0,100)