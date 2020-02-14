#include <iostream>

using namespace std;

int negative(uint32_t *ia, uint32_t *ob);

int main(){
	uint32_t a[10] = {64591051, 3172697395,0, 0,76157580, 46281898,1342177280, 48498273,3373798755, 4290117632};
	uint32_t aa[4];

    int i;

    negative(a,aa);

    for(i = 0; i < 1; i++){
    	cout << "a[" << i << "] = " << a[i] << " a[" << i << "] = " << a[i+1] << endl;
    	cout << "b[" << i << "] = " << a[i+2] << " b[" << i << "] = " << a[i+3] << endl;
    	cout << "W[" << i << "] = " << a[i+4] << " W[" << i << "] = " << a[i+5] << endl;
    	cout << "p[" << i << "] = " << a[i+6] << " p[" << i << "] = " << a[i+7] << endl;
    	cout << "pInv[" << i << "] = " << a[i+8] << " pInv[" << i << "] = " << a[i+9] << endl;
    	cout << "aa[" << i << "] = " << aa[i] << " aa[" << i << "] = " << aa[i+1] << endl;
        cout << "bb[" << i << "] = " << aa[i+2] << " bb[" << i << "] = " << aa[i+3] << endl;

    }
}
