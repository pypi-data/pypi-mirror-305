#pragma once
#include "Challenge.h"
#include <ctime>
#include <iostream>
#include <memory>
#include <stdlib.h>
#include <vector>

const int numberOfChallenges = 60 * 390;

class MarketData {
public:
  std::vector<std::shared_ptr<Challenge>> challenges;
  std::vector<float> buyPrices;
  std::vector<float> sellPrices;
  float startBuyPrice;
  float startSellPrice;
  int currentDay;

  MarketData(float sbp, float ssp) : startBuyPrice(sbp), startSellPrice(ssp) {
    ChallengeFactory::registerChallenges();
    srand(time(NULL));

    // normal
    for (int i = 0; i < 5000; i++) {
      ChallengeConfig config;
      config.challengeType = 5;
      config.volatility = 0.0015;
      config.drift = 0.00001;
      config.price_impact = 0.00001;
      config.volume_impact = 0.00001;
      config.day = i;
      config.k = 0.3;

      challenges.push_back(ChallengeFactory::createChallenge(config));
    }

    // News Shock
    for (int i = 5000; i < 10000; i++) {
      ChallengeConfig config;
      config.challengeType = 5;
      config.volatility = 0.002;
      config.drift = 0.00002;
      config.price_impact = 0.00001;
      config.volume_impact = 0.00001;
      config.day = i;
      config.s_base = 0.0006;
      config.k = 0.4;

      challenges.push_back(ChallengeFactory::createChallenge(config));
    }

    // High volume
    for (int i = 10000; i < 15000; i++) {
      ChallengeConfig config;
      config.challengeType = 5;
      config.drift = 0.00001;
      config.volatility = 0.0015;
      config.price_impact = 0.000008;
      config.s_base = 0.0004;
      config.k = 0.3;
      config.volume_impact = 0.000015;
      config.day = i;

      challenges.push_back(ChallengeFactory::createChallenge(config));
    }

    // flash crash
    for (int i = 15000; i < 17500; i++) {
      ChallengeConfig config;
      config.challengeType = 5;
      config.drift = -0.00002;
      config.volatility = 0.003;
      config.price_impact = 0.00002;
      config.s_base = 0.0008;
      config.k = 0.5;
      config.volume_impact = 0.00002;
      config.day = i;

      challenges.push_back(ChallengeFactory::createChallenge(config));
    }

    // calm
    for (int i = 17500; i < 20000; i++) {
      ChallengeConfig config;
      config.challengeType = 5;
      config.drift = 0.000005;
      config.volatility = 0.001;
      config.price_impact = 0.000005;
      config.s_base = 0.0003;
      config.k = 0.2;
      config.volume_impact = 0.000005;
      config.day = i;

      challenges.push_back(ChallengeFactory::createChallenge(config));
    }

    // liquidation crisis
    for (int i = 20000; i < 22500; i++) {
      ChallengeConfig config;
      config.challengeType = 5;
      config.drift = 0.00001;
      config.volatility = 0.002;
      config.price_impact = 0.00002;
      config.s_base = 0.0007;
      config.k = 0.4;
      config.volume_impact = 0.00002;
      config.day = i;

      challenges.push_back(ChallengeFactory::createChallenge(config));
    }

    // late day rush
    for (int i = 22500; i < numberOfChallenges; i++) {
      ChallengeConfig config;
      config.challengeType = 5;
      config.drift = 0.00002;
      config.volatility = 0.0018;
      config.price_impact = 0.00001;
      config.s_base = 0.0005;
      config.k = 0.3;
      config.volume_impact = 0.00001;
      config.day = i;

      challenges.push_back(ChallengeFactory::createChallenge(config));
    }

    init();
  }

  void init() {
    buyPrices.push_back(startBuyPrice);
    sellPrices.push_back(startSellPrice);
    currentDay = 0;
  }

  std::pair<float, float> getNextPrices(float buy, int vb, float sell, int vs) {
    if (currentDay >= numberOfChallenges) {
      return {-1, -1};
    }

    float prevBuyPrice = buyPrices.back();
    float prevSellPrice = sellPrices.back();

    Order o = {prevBuyPrice, buy, vb, prevSellPrice, sell, vs};

    std::pair<float, float> next = challenges[currentDay]->update(o);

    buyPrices.push_back(next.first);
    sellPrices.push_back(next.second);
    currentDay++;

    return next;
  }
};