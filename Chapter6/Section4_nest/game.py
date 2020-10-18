list = {
    0,1,0,
    1,1,0,
    0,1,1,
    }
    # include<stdio.h>
# include<math.h>
int main(void)
{
	int n[3][3] = {
		0,1,0,
		1,1,0,
		0,1,1
	};
	int x, y,m,b;
	while (true)
	{
		int t,i;
		scanf_s("%d", &m);
		scanf_s("%d", &b);
		x = m-1;
		y = b-1;
		if (x - 1 >= 0)
			if (n[x - 1][y] == 0) n[x - 1][y] = 1;
			else n[x - 1][y] = 0;
		if (y - 1 >= 0)
			if (n[x][y - 1] == 0) n[x][y - 1] = 1;
			else n[x][y - 1] = 0;
		if (y + 1 < 3)
			if (n[x][y + 1] == 0) n[x][y + 1] = 1;
			else n[x][y + 1] = 0;
		if (x + 1 < 3)
			if (n[x + 1][y] == 0) n[x + 1][y] = 1;
			else n[x + 1][y] = 0;
		if (n[x][y] == 0) n[x][y] = 1;
		else n[x][y] = 0;
		for (t = 0; t < 3;t++)
		{
			for (i = 0;i < 3;i++)
			{
				printf("%d ", n[t][i]);
			}
			printf("\n");
		}
	}
}
