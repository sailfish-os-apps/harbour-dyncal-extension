Name:          harbour-dyncal-ex
Version:       0.2.0
Release:       1
Summary:       DynCal MYCOUNTRY
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires: harbour-dyncal >= 0.3.0-1
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
Change Calendar icon accordingly with the day. It features MYCOUNTRY holidays.

%files
%defattr(-,root,root,-)
/usr/share/*

%post
mkdir /usr/share/harbour-dyncal-ex/backup
chmod +x /usr/share/harbour-dyncal-ex/run.sh
/usr/share/harbour-dyncal-ex/run.sh

%preun
cp /usr/share/harbour-dyncal-ex/backup/* /usr/share/harbour-dyncal/icons/

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/harbour-dyncal-ex
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
/usr/share/harbour-dyncal/harbour-dyncal.sh
fi
fi

%changelog
* Mon Dec 14 2015 0.2
- Backup handling improved.

* Tue Dec 8 2015 0.1
- First build.
