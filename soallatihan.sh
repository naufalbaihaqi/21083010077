# mendeklarasikan fungsi
panjang() {
       echo "masukkan panjang :"
       read p
}
lebar() {
     echo "masukkan lebar :"
     read l
}
luas() {
    echo "menghitung luas bidang persegi"
    panjang
    lebar
    let l=$p*$l
    echo "luas persegi :
$l"
}
# memanggil fungsi
luas
