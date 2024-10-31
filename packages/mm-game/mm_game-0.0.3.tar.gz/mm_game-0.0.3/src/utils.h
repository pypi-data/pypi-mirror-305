#pragma once
#include <cmath>
#include <corecrt_math_defines.h>
#include <cstdlib>
#include <random>
#include <stdlib.h>

namespace utils {
float random(float a, float b) {
  float random = ((float)rand()) / (float)RAND_MAX;
  float diff = b - a;
  float r = random * diff;
  return a + r;
}

// Function to generate a random number from a normal distribution
float normal(float mean = 0.0, float stddev = 1.0) {
  // Generate two uniform random numbers in the range (0, 1]
  float u1 =
      (rand() + 1.0) / (RAND_MAX + 2.0); // Add a small offset to avoid log(0)
  float u2 = (rand() + 1.0) / (RAND_MAX + 2.0);

  // Apply Box-Muller transform
  float z0 = sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2);

  // Scale and shift the result to get the desired mean and standard deviation
  return z0 * stddev + mean;
}

int generatePoisson(int lambda) {
  // Initialize random number generator with a random device as the seed
  std::random_device rd;
  std::mt19937 gen(rd());

  // Define Poisson distribution with mean lambda
  std::poisson_distribution<int> distribution(lambda);

  // Generate and return a single Poisson-distributed random value
  return distribution(gen);
}
} // namespace utils
