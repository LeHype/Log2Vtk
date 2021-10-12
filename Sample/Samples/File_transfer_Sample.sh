#!/bin/sh
PATHHOME='/home/heib/Documents/Sample/Samples/'
SERVERNAME='rechnen@zuse.ltm.uni-saarland.de'
PATHRECHNEN='/home/rechnen/heib/UEL/TEST_2/'
FILENAME='Dummy'
func1() {
   echo "Waiting for abaqus job"
   if sshpass -p "******"  ssh rechnen@zuse.ltm.uni-saarland.de stat heib/UEL/TEST_2/$FILENAME.lck \> /dev/null 2\>\&1
            then
                    sleep 2
                    func1
            else
                   
                    echo "proceding"

    fi
}
$pwd
sshpass -p "go3ein" scp $PATHHOME$FILENAME'.f' ssh $SERVERNAME':'$PATHRECHNEN
sshpass -p "go3ein" scp $PATHHOME$FILENAME'.inp' ssh $SERVERNAME':'$PATHRECHNEN
sshpass -p "go3ein"  ssh $SERVERNAME "cd $PATHRECHNEN ; abaqus job=$FILENAME user=$FILENAME'.f'"
func1


sshpass -p "go3ein" scp  ssh $SERVERNAME':'$PATHRECHNEN$FILENAME'.log' $PATHHOME
sshpass -p "go3ein" scp  ssh $SERVERNAME':'$PATHRECHNEN$FILENAME'.dat' $PATHHOME
sshpass -p "go3ein" scp  ssh $SERVERNAME':'$PATHRECHNEN$FILENAME'.sta' $PATHHOME
sshpass -p "go3ein" scp  ssh $SERVERNAME':'$PATHRECHNEN$FILENAME'.msg' $PATHHOME
sshpass -p "go3ein" scp  ssh $SERVERNAME':'$PATHRECHNEN$FILENAME'.odb' $PATHHOME




