Name:          harbour-dyncal-it
Version:       0.1.0
Release:       2
Summary:       DynCal Italy
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires: harbour-dyncal >= 0.3.0-1
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
Change Calendar icon accordingly with the day. It features Italian holidays.

%pre
mkdir /usr/share/harbour-dyncal/backup
cp /usr/share/harbour-dyncal/icons/*.* /usr/share/harbour-dyncal/backup/

%files
%defattr(-,root,root,-)
/usr/share/*

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
cp /usr/share/harbour-dyncal/backup/*.* /usr/share/harbour-dyncal/icons/
rm -rf /usr/share/harbour-dyncal/backup
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
/usr/share/harbour-dyncal/harbour-dyncal.sh
fi
fi

%changelog
* Thu Oct 8 2015 0.2.5
- Holidays' icons updated.

* Wed Oct 7 2015 0.2.4
- Icon jumping to the bottom of the app tray may be fixed.

* Sat Oct 3 2015 0.2.3
- Bugfix.

* Tue Sep 29 2015 0.2.2
- Bugfix.

* Tue Sep 29 2015 0.2.1
- Bugfix.

* Mon Sep 28 2015 0.2
- Added some holidays' icons.
- Fixed icon not updating.

* Thu Sep 22 2015 0.1
- First build.
