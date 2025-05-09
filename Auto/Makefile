#===> auto.makefile
#
#   Makefile written by Xianjun WANG in March 1994
#
#   This Makefile is called from the Graphic User Interface (GUI)
#
#   The following environment variables are controlled in GUI program 
#   at run time:
#
#   PROGRAMNAME        :     the name of the program
#   NEW_PROGRAMNAME    :     the output data name saved by "save as ..." button
#   NEW_PLOTNAME       :     the output data name to be plotted by "plot name ..." button
#   RESTARTNAME        :     the restart data name to be set to unit 3 (fort.3)
#   RESTARTDATA        :     same as RESTARTNAME, but only needed in GUI program
#   COPYFROM           :     the name of the output data to be copied from
#   COPYTO             :     the name of the output data to be copied to
#   MOVEFROM           :     the name of the output data to be moved from
#   MOVETO             :     the name of the output data to be moved to
#   APPENDFROM         :     the name of the output data to be appended from
#   APPENDTO           :     the name of the output data to be appended to
#   DELETEDATA         :     the name of the output data to be deleted
#   
#
.IGNORE:
#
FC    	   = gfortran
FFLAGS 	   = -g -fopenmp
OPT    	   = -O
SRC        = $(PROGRAMNAME).f
OBJ        = $(PROGRAMNAME).o
EXE        = $(PROGRAMNAME).exe
LIBS       = $(AUTO_DIR)/lib/*.o
RM         = rm -f
#
start: $(EXE) run
#
run:
	@echo " "
	@echo "Starting $(PROGRAMNAME) ..."
	@echo " "
	@cp c.$(PROGRAMNAME) fort.2
	@touch fort.3
	@./$(EXE)
	@rm -f fort.3
	@echo " "
	@echo "$(PROGRAMNAME) ... done"
#
restart: $(EXE) rerun
rerun:
	@echo " "
	@echo "Restarting $(PROGRAMNAME) ..."
	@echo " "        
	@cp c.$(PROGRAMNAME) fort.2
	@cp s.$(RESTARTNAME) fort.3
	@./$(EXE)
	@rm -f fort.3
	@echo " " 
	@echo "$(PROGRAMNAME) ... done"
#
$(EXE): $(OBJ)
	$(FC) $(FFLAGS) $(OPT) $(OBJ) -o $@ $(LIBS)
#
$(OBJ): $(SRC)
	$(FC) $(FFLAGS) $(OPT) -c $(SRC) -o $@
#
save:
	@echo " "
	@echo "Starting save ..."
	@cp fort.7  b.$(PROGRAMNAME)
	@echo "Saved fort.7 as b.$(PROGRAMNAME)"
	@cp fort.8  s.$(PROGRAMNAME)
	@echo "Saved fort.8 as s.$(PROGRAMNAME)"
	@cp fort.9  d.$(PROGRAMNAME)
	@echo "Saved fort.9 as d.$(PROGRAMNAME)"
	@echo "Saving ... done"
	@echo " "
#
saveas:
	@echo " "
	@echo "Starting save ..."
	@cp fort.7  b.$(NEW_PROGRAMNAME)
	@echo "Saved fort.7 as b.$(NEW_PROGRAMNAME)"
	@cp fort.8  s.$(NEW_PROGRAMNAME)
	@echo "Saved fort.8 as s.$(NEW_PROGRAMNAME)"
	@cp fort.9  d.$(NEW_PROGRAMNAME)
	@echo "Saved fort.9 as d.$(NEW_PROGRAMNAME)"
	@cp fort.2  c.$(NEW_PROGRAMNAME)
	@echo "Saved fort.2 as c.$(NEW_PROGRAMNAME)"
	@echo "Saving ... done"
	@echo " "
#
append:
	@echo " "
	@echo "Starting append ..."
	@cat fort.7 >> b.$(PROGRAMNAME)
	@echo "Appended fort.7 to b.$(PROGRAMNAME)"
	@cat fort.8 >> s.$(PROGRAMNAME)
	@echo "Appended fort.8 to s.$(PROGRAMNAME)"
	@cat fort.9 >> d.$(PROGRAMNAME)
	@echo "Appended fort.9 to d.$(PROGRAMNAME)"
	@echo "Appending ... done"
	@echo " "
#
appendto:
	@echo " "
	@echo "Starting append ..."
	@cat fort.7 >> b.$(NEW_PROGRAMNAME)
	@echo "Appended fort.7 to b.$(NEW_PROGRAMNAME)"
	@cat fort.8 >> s.$(NEW_PROGRAMNAME)
	@echo "Appended fort.8 to s.$(NEW_PROGRAMNAME)"
	@cat fort.9 >> d.$(NEW_PROGRAMNAME)
	@echo "Appended fort.9 to d.$(NEW_PROGRAMNAME)"
	@echo "Appending ... done"
	@echo " "
#
plot_current:
	@echo " "
	@echo "Starting plaut ..."
	@cp b.$(PROGRAMNAME) fort.17
	@cp s.$(PROGRAMNAME) fort.18
	@echo "Plotting b.$(PROGRAMNAME) and s.$(PROGRAMNAME) ..."
	@xterm -bg black -fg white -t -e $(AUTO_DIR)/bin/plaut
	@$(RM) fort.17
	@$(RM) fort.18
	@echo "Plotting ... done"
	@echo " "
#
plot_other:
	@echo " "
	@echo "Starting plaut ..."
	@cp b.$(NEW_PLOTNAME) fort.17
	@cp s.$(NEW_PLOTNAME) fort.18
	@echo "Plotting b.$(NEW_PLOTNAME) and s.$(NEW_PLOTNAME) ..."
	@xterm -bg black -fg white -t -e $(AUTO_DIR)/bin/plaut
	@$(RM) fort.17
	@$(RM) fort.18
	@echo "Plotting ... done"
	@echo " "
#
restartdata:
	@echo " "
	@echo "Setting s.$(RESTARTDATA) as restart file ... done"
#
copydata:
	@echo " "
	@cp b.$(COPYFROM) b.$(COPYTO)
	@echo "Copying b.$(COPYFROM) to b.$(COPYTO) ... done"
	@cp s.$(COPYFROM) s.$(COPYTO)
	@echo "Copying s.$(COPYFROM) to s.$(COPYTO) ... done"
	@cp d.$(COPYFROM) d.$(COPYTO)
	@echo "Copying d.$(COPYFROM) to d.$(COPYTO) ... done"
	@cp c.$(COPYFROM) c.$(COPYTO)
	@echo "Copying c.$(COPYFROM) to c.$(COPYTO) ... done"
#
appenddata:
	@echo " "
	@cat b.$(APPENDFROM) >> b.$(APPENDTO)
	@echo "Appending b.$(APPENDFROM) to b.$(APPENDTO) ... done"
	@cat s.$(APPENDFROM) >> s.$(APPENDTO)
	@echo "Appending s.$(APPENDFROM) to s.$(APPENDTO) ... done"
	@cat d.$(APPENDFROM) >> d.$(APPENDTO)
	@echo "Appending d.$(APPENDFROM) to d.$(APPENDTO) ... done"
#
movedata:
	@echo " "
	@mv -f b.$(MOVEFROM) b.$(MOVETO)
	@echo "Moving b.$(MOVEFROM) to b.$(MOVETO) ... done"
	@mv -f s.$(MOVEFROM) s.$(MOVETO)
	@echo "Moving s.$(MOVEFROM) to s.$(MOVETO) ... done"
	@mv -f d.$(MOVEFROM) d.$(MOVETO)
	@echo "Moving d.$(MOVEFROM) to d.$(MOVETO) ... done"
	@mv -f c.$(MOVEFROM) c.$(MOVETO)
	@echo "Moving c.$(MOVEFROM) to c.$(MOVETO) ... done"
#
deletedata:
	@echo " "
	@$(RM) b.$(DELETEDATA)
	@echo "Deleting b.$(DELETEDATA) ... done"
	@$(RM) s.$(DELETEDATA)
	@echo "Deleting s.$(DELETEDATA) ... done"
	@$(RM) d.$(DELETEDATA)
	@echo "Deleting d.$(DELETEDATA) ... done"
#
clean:
	@echo " "
	@echo "Cleaning ..."
	@$(RM) *.o fort.* *.exe *.trace core
	@echo "Cleaning ... done"
	@echo " "
#
# DO NOT ADD ANYTHING AFTER THIS LINE
#
