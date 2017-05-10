---
title: Intro to A/B Testing
duration: "1:25"
creator:
    name: Robby Grodin
    city: BOS
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to A/B Testing
Week 11 | Lesson 1.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Identify the use cases for A/B testing
- Analyze the results of A/B tests using different tests for statistical significance

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Recall the means by which we auditioned different algorithms

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Familiarize yourself with the Case Studies in the lesson plan, or, find others you wish to use
- Provide students with additional resources

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Opening  |
| 10 min  | [Introduction](#introduction)  | A/B Testing  |
| 15 min  | [Introduction](#intro-design)  | A/B Test Design  |
| 5 min  | [Introduction](#intro-analysis)  | Test Analysis Strategies  |
| 10 min  | [Demo](#demo-ttest)  | _T_-tests  |
| 10 min  | [Guided Practice/Codealong](#code-ztest)  |  _Z_-tests  |
| 10 min  | [Introduction](#intro-multi)  |  Multi-Variate Testing  |
| 10 min  | [Discussion](#discussion1)  | A/B Test Case Study 1 - Obama's Fundraising Campaign  |
| 10 min  | [Discussion](#discussion2)  | A/B Test Case Study 2 - AMD's Social Media Sharing  |
| 5 min  | [Conclusion](#Conclusion)  | Conclusion  |
---

<a name="opening"></a>
## Opening (5 mins)

Welcome to week 11! This week, we will be focusing mostly on outcomes and your capstone. Regarding outcomes, this lesson will cover a very important practice that most technology companies struggle with, but with the aid of a Data Scientist the results can be greatly improved.

We've spent a lot of time trying to frame the use of our models in a real-world context. We're going to give you a scenario that can be done in many different ways, and will ask you to consider the ways in which statistical inference can aid in analysing the data. Get your Data Scientist hats on, it's time to A/B test!

**Check:** Does anyone have any experience with A/B testing? What was the situation in which you conducted an A/B test, and how did you analyse the results?

<a name="introduction"></a>
## Introduction: A/B Testing (10 mins)

Throughout the past 10 weeks, you've trained quite a few models. In some labs and exercises, you've likely trained multiple models for a single data set. How did you evaluate the models? Is there one right way to choose a best fit model?

In most cases, you likely created a derived data set from each of your models. This might be in the form of residuals, confidence scores, or predictions. By compared derived data sets from two different models, you've effectively utilized a common technique called A/B testing. Whether you're funneling data through two different models, or showing users two different versions of a website, A/B testing is the means by which we can compare two versions of similar concepts.

> A/B Testing is a term for a randomized experiment with two variants, A and B. These tests consist of test design, data collection, and data analysis stages.

The most common use of A/B testing is to audition proposed changes to a website. Once the variants are designed, data is collected by assigning users to 'test' and 'control' groups, which will dictate the version of the site they will be served. The data that is collected is then analysed to decide if the change should be pushed to the site.

An example of this is shown in the below graphic taken from www.vwo.com, a third parting A/B testing utility.

![](./assets/images/ab_test1.png)

It's very important when designing an A/B test to make the smallest change possible before testing the variant. Widespread changes introduce a slew of variables that will be impossible to track in most cases. Some examples of A/B tests that one might conduct are:

- Changing the number of images on a page
- Changing the font on a page
- Adding or removing single elements from a page
- Altering the text on a button
- Re-organizing a pages content

**Check:** Consider an e-commerce site. What must be taken into account when designing, conducting, and analysing an A/B test?

> Answer: The main effect in e-commerce is the flow of the user through the conversion funnel. Once users land on the site, test to see if the variant has any effect on how many products they view, how many products are added to cart, changes in cart abandonment rates, changes in conversion rates, order volume, average order value, etc.

**Check:** Look back on some of the projects from previous weeks. Are any of them reminiscent of A/B tests? What have we learned that would be useful in these types of tests?

<a name="intro-design"></a>
## Introduction: A/B Test Design (15 mins)

An A/B test is only as good as its design. Designing the test involves asking these four questions:

### 1. What element(s) will be changed?

While working with a PM, you will likely have little say in what elements are changed for a test. Keep in mind that to prevent false correlations in the data, the smallest changes possible will likely have the most meaningful results.


### 2. Who will be a part of the test group?

Will you be splitting the incoming traffic 50/50 between variants, or can you get away with serving the variant under test to a smaller group? Also, will the test split change? We'll discuss one strategy for assigning test groups in the next section.

### 3. How long will the test run?

This is a very important question to ask. If the test doesn't run long enough, your data won't be useful. If it runs too long, that can impact business needs. 
Remember back to Week 9's Time Series Analysis lessons- ensure that you have enough data to capture across multiple periods, or seasons, but not too much data that your result will be heavily affected by trend.

### 4. Why is this test truly necessary?

A/B testing is a gamble. If the business result of the test is less valuable than the possible negative effects on churn or conversion rate, then it might be worth re-evaluating your design.

## Multi-Arm Bandit Testing

A traditional A/B test is done by splitting traffic between variants 50/50. A newer approach is the _Multi-Arm Bandit_. 

In this strategy, traffic is split as such:
- **Exploration Phase**: During the first ~10% of the test, traffic is split 50/50. This phase picks a short-term 'winner', and a short-term 'loser'.
- **Exploitation Phase**: For the remainder of the test, shift the majority of traffic to the higher performing variant. Continue to adjust traffic as performance increases/decreases.

The Multi-Arm Bandit approach is championed by many big companies, primarily Google. In the [Additional Resources](#add-res) section below, there's a nice article on Google's strategy.

**Check:** What do you think the pros and cons of this model are?

In practice, Multi-Arm Bandit testing does a fairly good job of optimizing conversion rates. The downside to this method, however, is increased difficulty in evaluation of results. Simply picking a 'winner' variant is not always the best strategy, especially since the 'loser' variant often gets so little traffic that it can be hard to validate the statistical significance of the lift. 

To shed more light on the importance of controlling your traffic flow through variants, let's look at how these tests are analyzed.


<a name="intro-analysis"></a>
## Introduction: Test Analysis Strategies (5 mins)

**Check:** How do you think we would analyse the results of an A/B test?

Consider an e-commerce example. Two variants are created, and after the appropriate data collection period has passed, you've found that the test variant has a higher conversion rate than the control. Does that automatically mean that the variant is better? Why or why not?

There are many means by which we can analyse the results of our test. They are not always interchangeable, as some heuristics are more meaningful than others given the circumstance. The end result is usually the same- to test whether or not the difference between variants is statistically significant, or if it is just a fluke.

<a name="demo-ttest"></a>
## Demo: _T_-tests (10 mins)

Also referred to as the Student's _t_-test, it is one of the most commonly used techniques for testing a null hypothesis on the basis of a difference between sample means. By testing the means of two samples derived from the same source, the _t_-test determines a probability that two populations are the same with respect to the variable tested. In an A/B test, this will tell us if the difference in the target metric is accidental, or _statistically significant_.

![](./assets/images/ttest-formula.png)

**Check:** The output of a _t_-test is a _p_ value. Do you recall the significance of _p_ values? What range of _p_ values indicate statistical significance?

_t_-tests can be either _one-tailed_ or _two-tailed_. This refers to whether or not the change is measure in two directions, or only one. Visually, this looks like:

**One-Tailed**:
![one-tailed](./assets/images/1tailed.gif)

**Two-Tailed**:
![two-tailed](./assets/images/2tailed.gif)


Let's look at how we would model the Student's _t_-test in Python in the [`ab_testing.ipynb`](./assets/code/solution-code/ab_testing.ipynb) notebook.



<a name="code-ztest"></a>
## Guided Practice/Codealong: _Z_-tests (15 mins)

The _z_-tests is another method used to analyse test results. Use of a _z_-test is possible when the observed data can be decided to follow a Normal distribution with _unknown mean_ and _known variance_. The output of a _z_-test is the _z_-statistic, which represents the number of standard deviations  and its corresponding _p_-value. It is defined as such: 

![](./assets/images/ztest-formula.png)

While `statsmodels` does have a built in method for calculating _z_ values, we're going to build our own based on the above formula. Let's open the [`ab_testing.ipynb`](./assets/code/solution-code/ab_testing.ipynb) notebook now.



<a name="intro-multi"></a>
## Introduction: Multi-Variate Testing (10 mins)

Rather than testing changes one at a time in serial, it can be useful to test multiple variants in parallel. This is called Multi-Variate Testing. The goal of this strategy is to quickly detect the ideal combination of components by trying out all possible combinations at once.

Here's a toy website that we want to try a Multi-Variate test on.

![](./assets/images/toy.png)

Here are the four variants we would like to try:

| Variant  | Image  | Title  |
|:-:|---|---|
| Control  | Stars  | General Assembly DSI  |
| Test 1  | Flowers  | General Assembly DSI  |
| Test 2  | Stars  | Data Science Immersive  |
| Test 3  | Flowers  | Data Science Immersive  |

This test would be set up the same as a typical A/B test, with each variant getting roughly 25% of the traffic. There is a clear downside to this, however, as it would take a higher amount of time and traffic to get statistically significant results. 

Another downside to Multi-Variate testing is that sometimes one of the variables has little effect on conversion rates, or other indicators of success. For example, if changing our toy site's Image has a noticeable effect on conversion, but the change on the Title does not, we would have been better off setting up the test as an A/B. The ineffective variable will only serve to cloud our results, possibly preventing us from rejecting the null hypothesis. 

Evaluating these tests can be done in multiple ways, and it's up to the analyst to determine the best fit. ANOVA is the most commonly used test, but results can also be analysed using an ensemble of _t_-tests.

<a name="discussion1"></a>
## Discussion: A/B Test Case Study 1 - Obama's Fundraising Campaign (10 mins)

One of the most popular case studies of A/B testing in recent memory was posted by [Optimizely](https://www.optimizely.com/) on their company blog. Optimizely is a 3rd party A/B testing tool which allows you to easily design, serve, and analyze website optimization tests. 

Go ahead and read the article [here](https://blog.optimizely.com/2010/11/29/how-obama-raised-60-million-by-running-a-simple-experiment/), and get ready to discuss afterwards.

Now that we've read the article, let's discuss. 

> Instructor's Note: Here are a few prompts. 
> - Why do you think this test worked?
> - What were the risks taken? Were they worth taking?
> - What next steps would you have taken if this test were still going?


<a name="discussion2"></a>
## Discussion: A/B Test Case Study 2 - AMD's Social Media Sharing (10 mins)

A/B testing is a great way to continuously mine data about what people are interested in on social media. This next case study is about AMD, a semiconductor company responsible for creating some of the hardware that is likely in the computer you're using right now. In this case study, we will see how a simple change in placement had a major increase on social media sharing.

Go ahead and read the article [here](https://vwo.com/blog/amd-3600-social-sharing-increase/), and get ready to discuss afterwards.

Now that we've read the article, let's discuss. 

> Instructor's Note: Here are a few prompts. 
> - Why do you think this test worked?
> - What were the risks taken? Were they worth taking?
> - What next steps would you have taken if this test were still going?

https://vwo.com/blog/amd-3600-social-sharing-increase/


<a name="conclusion"></a>
## Conclusion (5 mins)

A/B Testing is a key opportunity for Data Scientists to have a concrete effect on business outcomes. It requires more than just statistical formulas, as one must call on their business intuition and technical competency to full understand the results. The design, implementation, and analysis of an A/B test will typically be performed across functions, putting the Data Scientist in close contact with PM's, developers, and UX designers. If this kind of thing interests you, it would be a good idea to take some time and try out the third party tools that are available to you, such as Optimizely, Sitespect, VWO, etc. Many of them have demos on their sites, or if you're interested in web development, take the time to put together your own A/B testing tools. 

> Instructor's Note: Take this time to field any questions, and ensure students are prepared for the corresponding lab next session.

***

<a name="add-res"></a>
### ADDITIONAL RESOURCES

- [Google's Multi-Arm Bandit Strategy](https://support.google.com/analytics/answer/2844870?hl=en)
- [A/B Testing Case Studies](https://www.whichtestwon.com/case-studies/)
