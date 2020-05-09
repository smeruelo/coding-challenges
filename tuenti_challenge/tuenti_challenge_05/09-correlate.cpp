/*#include "findScore.hpp" */

#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))
#define MAX(X,Y) ((X) < (Y) ? (Y) : (X))
#define THRESCORR 1e-30

#include <vector>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <iomanip>

using namespace std;

std::vector<double> crosscorr(const double* x, int xSize, const double * y, int ySize, const double yMean, const double ySumCuadraticDiff)
{
	std::vector<double> xcorr;

	//! Calculate the mean of the two series x[], y[]
	double xMean = 0.0;
	for (int i = 0; i < xSize; i++) {
	  xMean += x[i];
	}
	xMean = xMean / xSize;

	//! Calculate the denominator (product of standard deviations)
	double xSumCuadraticDiff = 0.0;
	for (int i = 0; i < xSize; i++) {
		xSumCuadraticDiff += pow(x[i] - xMean, 2);
	}

	double denom = sqrt(xSumCuadraticDiff * ySumCuadraticDiff);
	if (denom < THRESCORR){
		xcorr.resize(0);
		return xcorr;
	}

	//! Calculate the correlation series
	xcorr.resize(ySize - xSize + 1);
	for (int delay = 0; delay < xcorr.size(); delay++) {
		double xySum = 0.0;
		for (int i = 0; i < xSize; i++) {
			xySum += (x[i] - xMean) * (y[i + delay ] - yMean);
		}
		xcorr[delay] = xySum / denom;
	}
	return xcorr;
}

double patternMean(const double* pattern, int ySize)
{
  double yMean = 0.0;
  for (int i = 0; i < ySize; i++) {
      yMean += pattern[i];
  }
  yMean = yMean / ySize;
  return yMean;
}

double patternSumCuadraticDiff(const double* pattern, int ySize, double yMean)
{
  double ySumCuadraticDiff = 0.0;
  for (int i = 0; i < ySize; i++) {
    ySumCuadraticDiff += pow(pattern[i] - yMean, 2);
  }
  return ySumCuadraticDiff;
}


double findScore(const double* wave, int waveSize, const double* pattern, int patternSize)
{
  double score = 0.0;
  int minSubvectorLength = 2;
  double yMean = patternMean(pattern, patternSize);
  double ySumCuadraticDiff = patternSumCuadraticDiff(pattern, patternSize, yMean);

  for (int subvectorStart = 0; subvectorStart <= waveSize - minSubvectorLength; subvectorStart++) {
    for (int subvectorLength = minSubvectorLength; subvectorLength <= MIN(waveSize - subvectorStart, patternSize); subvectorLength++) {
      std::vector<double> xcorrelation = crosscorr(&(wave[subvectorStart]), subvectorLength, pattern, patternSize, yMean, ySumCuadraticDiff);

      for (int xcorrelationIndex = 0; xcorrelationIndex < xcorrelation.size(); xcorrelationIndex++) {
	score = MAX(score, xcorrelation[xcorrelationIndex] * subvectorLength);
      }
    }
  }

  return score;
}



int main (void){

  int P, W, i;
  cin >> P >> W;

  double pattern[P];
  double wave[W];
  double result;

  for (i=0;i<P;i++){
    cin >> pattern[i];
  }
  for (i=0;i<W;i++){
    cin >> wave[i];
  }

  result = findScore(wave, W, pattern, P);
  cout << setprecision(4) << fixed << result << endl;

}
