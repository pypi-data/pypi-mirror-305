#pragma once
#include "utils.h"
#include <cmath>
#include <functional>
#include <memory>
#include <unordered_map>

struct ChallengeConfig {
  int challengeType;
  float volatility;
  float drift;
  float price_impact;
  float volume_impact;
  int day;
  float s_base;
  float k;

  ChallengeConfig(int type, float vol, int d)
      : challengeType(type), volatility(vol), day(d) {}

  ChallengeConfig(int type, float vol, float dr, float pi, float vi, int d,
                  float _k = 0.5, float _s_base = 0.0005)
      : challengeType(type), volatility(vol), drift(dr), price_impact(pi),
        volume_impact(vi), day(d), k(_k), s_base(_s_base) {}

  ChallengeConfig() : challengeType(0), volatility(0), day(0) {}
};

struct Order {
  float buyPrice; // previous buy price
  float mmBuyPrice;
  int volumeBuy;
  float sellPrice; // previous sell price
  float mmSellPrice;
  int volumeSell;
};

class Challenge {
public:
  Challenge(ChallengeConfig &config) {};
  virtual std::pair<float, float> update(Order &o) = 0;
};

class Challenge0 : public Challenge {
public:
  Challenge0(ChallengeConfig &config) : Challenge(config) {}
  std::pair<float, float> update(Order &o) override {
    return {o.buyPrice, o.sellPrice};
  };
};

class Challenge1 : public Challenge {
private:
  float volatility;

public:
  Challenge1(ChallengeConfig &config)
      : Challenge(config), volatility(config.volatility) {};
  std::pair<float, float> update(Order &o) override {
    return {o.buyPrice * volatility, o.sellPrice * volatility};
  }
};

class Challenge2 : public Challenge {
private:
  float volatility;

public:
  Challenge2(ChallengeConfig &config)
      : Challenge(config), volatility(config.volatility) {};
  std::pair<float, float> update(Order &o) override {
    // generate some noise that is within 10% of val
    float val1 = o.buyPrice;
    float val2 = o.sellPrice;
    float noise1 = utils::random(-val1 / 50, val1 / 50);
    float noise2 = utils::random(-val2 / 50, val2 / 50);

    val1 += noise1;
    val2 += noise2;

    float change1 = val1 * volatility;
    float change2 = val2 * volatility;

    // Randomly change the sign of the change
    if (utils::random(0, 1) > 0.5) {
      change1 = -change1;
    }
    if (utils::random(0, 1) > 0.5) {
      change2 = -change2;
    }

    return {val1 + change1, val2 + change2};
  }
};

class Challenge3 : public Challenge {
private:
  float vol;
  float amplitude;
  float phase;
  int day;

public:
  Challenge3(ChallengeConfig &config)
      : Challenge(config), vol(config.volatility), amplitude(1.0), phase(0.0),
        day(config.day) {}

  std::pair<float, float> update(Order &o) override {

    float val1 = o.buyPrice;
    float val2 = o.sellPrice;

    float noise1 = utils::random(-val1 * vol, val1 * vol);
    float noise2 = utils::random(-val2 * vol, val2 * vol);

    val1 += noise1;
    val2 += noise2;

    float sineValue1 = amplitude * std::sin(day);
    float sineValue2 = amplitude * std::sin(day);

    return {val1 + sineValue1, val2 + sineValue2};
  }
};

class Challenge4 : public Challenge {
private:
  float changeRate;

public:
  Challenge4(ChallengeConfig &config)
      : Challenge(config), changeRate(config.volatility) {}

  std::pair<float, float> update(Order &o) override {
    float val1 = o.buyPrice;
    float val2 = o.sellPrice;

    float noise1 = utils::random(-val1 * changeRate, val1 * changeRate);
    float noise2 = utils::random(-val2 * changeRate, val2 * changeRate);

    val1 += noise1;
    val2 += noise2;

    if (changeRate > 0.0) {
      return {val1 + val1 * changeRate, val2 + val2 * changeRate};
    }

    return {val1 - val1 * changeRate, val2 - val2 * changeRate};
  }
};

class Challenge5 : public Challenge {
private:
  float volatility;    // sigma
  float drift;         // mu
  float price_impact;  // alpha
  float volume_impact; // beta
  int day;
  float theta;
  float s_base;
  float k;
  float P_fundamental;

public:
  Challenge5(ChallengeConfig &config)
      : Challenge(config), volatility(config.volatility), drift(config.drift),
        price_impact(config.price_impact), volume_impact(config.volume_impact),
        day(config.day), k(config.k) {
    theta = 0.001;
    s_base = config.s_base;
    P_fundamental = 100;
  }

  std::pair<float, float> update(Order &o) override {
    float epsilon = utils::normal(0, 1.0); // Standard normal noise

    float p = (o.buyPrice + o.sellPrice) / 2;

    float log_return = drift - 0.5 * volatility * volatility +
                       volatility * epsilon +
                       theta * (log(P_fundamental) - log(p));

    float P_t = p * exp(log_return);

    float bid_size = utils::generatePoisson(5000) + o.volumeBuy;
    float ask_size = utils::generatePoisson(5000) + o.volumeSell;

    float P_adjusted = P_t * (1 + price_impact * (bid_size - ask_size));
    float spread =
        s_base + k * volatility + volume_impact * abs(bid_size - ask_size);

    float bidPrice = P_adjusted * (1 - spread / 2);
    float askPrice = P_adjusted * (1 + spread / 2);

    return {bidPrice, askPrice};
  }
};

using ChallengeCreator =
    std::function<std::shared_ptr<Challenge>(ChallengeConfig &)>;

class ChallengeFactory {
private:
  static std::unordered_map<int, ChallengeCreator> challengeMap;

public:
  static void registerChallenge(int type, ChallengeCreator creator) {
    challengeMap[type] = creator;
  }

  static std::shared_ptr<Challenge> createChallenge(ChallengeConfig &config) {
    if (challengeMap.find(config.challengeType) == challengeMap.end()) {
      return std::make_shared<Challenge0>(config);
    }

    return challengeMap[config.challengeType](config);
  };

  static void registerChallenges() {
    registerChallenge(0, [=](ChallengeConfig &config) {
      return std::make_shared<Challenge0>(config);
    });

    registerChallenge(1, [=](ChallengeConfig &config) {
      return std::make_shared<Challenge1>(config);
    });

    registerChallenge(2, [=](ChallengeConfig &config) {
      return std::make_shared<Challenge2>(config);
    });

    registerChallenge(3, [=](ChallengeConfig &config) {
      return std::make_shared<Challenge3>(config);
    });

    registerChallenge(4, [=](ChallengeConfig &config) {
      return std::make_shared<Challenge4>(config);
    });

    registerChallenge(5, [=](ChallengeConfig &config) {
      return std::make_shared<Challenge5>(config);
    });
  }
};

std::unordered_map<int, ChallengeCreator> ChallengeFactory::challengeMap;