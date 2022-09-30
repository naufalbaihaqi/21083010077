 select minuman in popice nutrisari susu air kopi semua gajadibeli
 do
   case $minuman in
     popice|nutrisari|susu|semua)
          echo "maaf, habis"
      ;;
     air|kopi)
       echo "tersedia"
     ;;
     gajadibeli)
       break
     ;;
     *) echo "tidak ada di daftar menu"
     ;;
   esac
 done
