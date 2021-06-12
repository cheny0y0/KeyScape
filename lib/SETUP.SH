clear
echo
echo " KeyScape Setup"
echo
echo "  Input the location would you like to install, or press Ctrl-C to exit"
echo "  the Setup:"
read tempans
mkdir $tempans
cp ./I386/KEYSCAPE.PY $tempans
echo
echo " Installation completed successfully."
echo " Type \"python $tempans\" if you are using Python 2.x,"
echo " or \"python3 $tempans\" if you are using Python 3.x to run the game."
echo "Press Enter to exit the Setup..."
read
