#include <stdint.h>
int negative(uint32_t *ia, uint32_t *oa)
{
#pragma HLS INTERFACE m_axi depth=10 port=ia offset=slave
#pragma HLS INTERFACE m_axi depth=10 port=oa  offset=slave
#pragma HLS INTERFACE s_axilite port=return

	uint64_t a = 0;
	uint64_t b = 0;
	uint64_t W = 0;
	uint64_t p = 0;
	uint64_t pInv = 0;

	a = a + ia[0];
        a = a << 32;
	a = a + ia[1];

	b = b + ia[2];
	b = b << 32;
	b = b + ia[3];

	W = W + ia[4];
	W = W << 32;
	W = W + ia[5];

	p = p + ia[6];
	p = p << 32;
	p = p + ia[7];

	pInv = pInv + ia[8];
	pInv = pInv << 32;
	pInv = pInv + ia[9];


	unsigned __int128 U = static_cast<unsigned __int128>(b) * W;
	uint64_t U0 = static_cast<uint64_t>(U);
	uint64_t U1 = U >> 64;
	uint64_t Q = U0 * pInv;
	unsigned __int128 Hx = static_cast<unsigned __int128>(Q) * p;
	uint64_t H = Hx >> 64;
	uint64_t V = U1 < H ? U1 + p - H : U1 - H;
	b = a < V ? a + p - V : a - V;
	a += V;
	if (a > p) a -= p;


	oa[1] = a;
        a = a >> 32;
	oa[0] = a;
	oa[3] = b;
	b = b >> 32;
	oa[2] = b;

	return(0);
}
