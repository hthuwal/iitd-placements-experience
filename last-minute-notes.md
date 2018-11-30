# Publications

## Sign Language Gesture Recognition

### Problem

- Classify Argentinian Sign Language Video Gestures.
- 46 Gestures: 50 videos per category.
- 75% Train (40), 25% Test(10)

### Methodology

- Extract the frames from video sequences.
	+ Set max number of frames to 200: Repeat the last frame if required.
	+ Remove Background: In videos the people were wearing colored gloves.
	+ OpenCV

- Learning the spatial feature.
	+ Used Inception Model (Transfer Learning)
	+ Retrain Inception V3 by popping out the final layer placing our own.
	+ Label for each frame of the video is the label of the video itself.
	+ The idea was that the model inception will be able to learn spatial features corresponding to a gesture.
	
	+ Method 1
		* Each video -> sequence of frames -> sequence of predictions (43 dimensional) (by inception).
		* Each video 200 x 46 dimensional vector.
 
 	+ Method 2
 		* Each video -> sequence of frames -> sequence of pool layer outputs (2048 dimensional)
 		* Each video 200 x 2048 dimensional vector.

- Learning the temporal features
	+ Simple LSTM Based Model
	+ Used dropout.
	+ Input Layer | LSTM 256 as hidden dimension | Softmax Layer | Regression
	+ Cateogrical cross entropy loss.
	+ adam optimizer.

### Results

- Method 1: 80.87%
- Method 2: 95.21%

## Sign Language Character Recognition

### Problem

- Classify American Sign Language Characters images
- 36 Characters (26 + 10): 70 images per category
- 55 images per category for training, 15 images per category for testing

### Methodology

- Non Neural
	+ Image Segmentation. Extract skin color.
		+ converted to YIQ and YUV color space and retain pixels that cross a certain threshold.
	+ Feature Extraction.
		* Use SIFT (128 dimensional feature vectors) per image
		* K mean clustering of features of all images
		* Image -> 128 dimensional feature -> 128 dimensional (cluster number for each feature)
		* Histogram of each image.
		* Data = Histogram, label
	+ SVM
		* Optimum c and gamma using cross validation

- Neural
	+ Image augmentation
		* Shearm zoom, shifts
	+ Zero mean and unit variance.
	+ VGG 16 CNN
		* Pop out final layer
		* replace it with softmax layer with 36 channels
 
### Results

	- Non Neural: 44.259%
	- Neural: 95.50%

# MTP: AI2 Reasoning Challenge

- QA system that can answer Science MCQ Questions.
- ~7700 Questions
	+ Easy: Easily answerable using either an retrieval-based system or pmi based (co occurrence)
	+ Difficult: Rest
- Corpus: 14 Million science related sentences.

- Best recent:
	+ Non Neural: 
	+ Reading Strategies (42%)
		* Two Networks: Back and Forth Reading.
		* Highlights: special noun and adjective embeddings.
		* Fine Tuned Google Transformer Network + strategies.
		* Attention is all you need.
	+ ET-RR -> Microsoft
	+ BiLSTM Max-out -> 33.87 . Neat

- Reference DGEM (27.11 / 26.41)
	+ Elastic Search
		* Index Corpus 
		* Get support sentences for each Qi and Ai pair
	+ Ask DGEM (Decompositional Graph Embedding Model)
		* support(premise) entails hypothesis?
	+ Correct answer is option with highest entailment score.

- Tried Other Corpus
	+ Downloaded the NCERT / WebCHild
	+ No improvement

- Manual Analysis of Corpus
	+ Data is present
	+ May require multihop inference

- Problems with DGEM Pipeline
	+ Poor support sentences
	+ Corpus is not organized

- Try developing first a non neural approach (mentor's opinion)
	- Stanford openIE to create Graph
	- Naively match the corpus graph and the hypothesis graph.
	- Fraction of number of nodes.
	- Use Jaccard Distance, Euclidean Distance
	- 28.380 %

- Currently working on
	+ Analysis of the graphs created.
	+ Improving the graph and the inference algorithm.
	+ Collapse Jaccard similar nodes.


# Minor: Internal Localization

- Localization of wireless devices
	+ Based on Probe Requests received at AP
- Probe: A wifi enabled device continuously searches for access points
	+ Mac ID, signal strength, timestamp
- In collaboration with I2e1
- Data:
	+ Historical data of devices on site
	+ Validation data
		* Field visit. Paths with multiple checkpoints
		* Measure Exact **Location**
- distance = 10 ^ (P0 - P / 10*epsilon)
- Metric: RMSE
- Heuristics (Shapely for geometrical calculations)
	+ Centroid of intersection of 3 circles.
	+ Weighted centroids of intersection of 2 circles. Weight = 1/(r1*r2)
	+ Weighted centroid of centers of circles.

- Using Downhill Simplex Algorithm
	+ Minimize Sum over all four AP's `P0 - RSSIi - 10 epsilon log ( sqrt((x-xi)^2 + (y-yi)^2) )`


- Fingerprinting
	+ Closest point (euclidean distance) from existing points.
	+ Better Results.
	+ offline, not felxible, update is not easy

- HMM Model
	+ Location at time t dependent on Location at time t-1
	+ Location is observed variable and and is noisy
	+ Gaussian Emissions, Gaussian Transitions, Descritized state space.

- Kalman Filters
	+ Continuous state variables
	+ Gaussian transition probabilities and Gaussian Emission Probabilities

# Rap Lyrics Generation

- Ghostwriting Rap Lyrics:
	+ Write lyrics for an artist similar in style to artist but different than the existing lyrics.

- Dataset
	+ Fabolous artist 
	+ Only 191 songs

- Baseline Model
	+ V X 150 Embedding Layer
	+ LSTM 2 Layer's hidden dimension: 100
	+ Decode Layer: 100 x V
	+ Softmax output

- Use character Embeddings
	+ 100 Characters.
	+ 128 dimensional.
	+ LSTM with hidden dimension: 128
	+ Decode Layer: 128 x 100

- Use Pretraining:
	+ Pretrain on Kaggle Dataset

- Metrics:
	+ Rhyme density: Number of rhymed syllables / total number of syllables
	+ Low similarity: TF-IDF + Cosine Similarity
	+ Generate lyrics with same rhyme density but low similarity.


# ML Assignments

- Neural Networks
- Linear Regression
- Navie Bayes
- GDA
- Decison Trees
- K-means

# NLP Assignments

- Sentiment Categorization
	+ Non Neural
		+ Three levels of sentiments
		+ Convert reviews to: tfidf vectors
		+ Use SVM over them.

	+ Neural
		* CNN Architectures
		* Used 300 Dimensional Embeddings
		* embedding | dropout | conv1d + relu + maxpool + dropout | x 3 | out
		* cross entropy loss

- CRF 
	+ sklearn crfsuite
	+ NER system

# UAI Assignments

- EM in C++
- Given a Bayesian Netwrok in .bif format
- Learn Probability values using data. Some Data values are also missing.

# P2P cryptocurrency simulator

## Problem

- Implement a DHT to store keypairs.
- Two phase commit protocol to do Txn.
- Sender broadcasts committed Txns
- Receiver verifies the signatures
- ~Virtual Synchrony, double spend~

## Modules

- Datagram RPC Protocol
	+ Using asyncio.DatagramProtocol
		* override connection_made
		* override datagram_received
			- Do as requested

- Routing Table
	- Buckets: Ordered dicts
		-  Number of bits in hash
		-  which bucket? decided by highest bit set in the distance
		-  distance: xor
			+  Why XOR?
				*  Symmetric
				*  Traingle Inequality
		- update peer
			+ If new peer added, add into replacement caches
		
		- Forget peer
			+ Remove from bucket, add from replacement caches
		
		- Find closest peers
			+ Same thing works for both the node and values


# Analysis of GitHub data

## Stack

- HDFS
	- To store data
- Spark
	- To perform analysis
- Jupyter Notebooks
	- As the means of running queries
- Plotting
	- d3.js
	- bokeh
	- matplotlib

## Installation of HDFS & Spark

- Various issues on the cluster
- First we were trying out MapReduce / YARN but we couldn't set it up
- Setup standalone Spark on laptop
- Once that worked, we did it on Baadal as well
- YARN wasn't required - Spark handled it all

## Dataset: GHTorrent

- 60 GB compressed - 225 GB uncompressed
- 20 CSV files
- We did analysis on 9 files
- 94 GB

### Preprocessing

- xsv tool to remove columns we weren't interested in
- We did this locally
	- Only because we didn't have permanent access to Baadal
	- So we shortened it first and then uploaded (via LAN etc.)
- After preprocessing: 55 GB

## Analysis of github data

- Users: 20 million
- Exponential growth
	- from 2008 to 2017
	- `users.select(F.year('created_at').alias('year')).groupBy(year).count()`
	- `SELECT COUNT(*) FROM USERS GROUP BY YEAR('created_at')`
- New users per year-month
	- `GROUP BY YEAR('created_at'), MONTH('created_at')`
- User distribution
	- Global, India
	- GROUP BY 'country_code'
- Organizations
	- Global, Indian
	- Parameters
		- Number of employees
		- Followers per employee
		- Stars per employee
- Users at IITs
	- `company.name.startswith("IIT | INDIAN").groupBy('company').count()`
- Activities
	- Commit patterns of users
		- Number of comits - Time of day vs Day of Week
		- People had varying punchcards - some work in day / night etc.
	- Community participation
		- No. of projects vs % Community participation
			- Normal curve
		- `SELECT ceiling(100 * commits_by_others / total_commits) as community_part, COUNT(*) as num_repos GROUP BY project_id`
	- Most had 0%
		- Showed bus factor - 1
	- Programming language popularity by Code size!
		- Lame metric
		- We were trying to see if Java will come on top Because it is verbose
		- But, C came on top, followed by JS, Java, PHP, Python, Ruby project_languages table

Schema of the tables
	- Users, Followers, Projects, Stars,
	- Project Language, Project Members,
	- Commits, Issues, Pull Requests

## Ludo Bot

- Relative and absolute positions
- Some work best on relative and some on best.
- 
- Algorithm: Priority based
	1. coins to finish
	2. open
	3. can kill
	4. save yourself
	5. Move fartheset or second farthest
		- Choose whichever on mving reduces threat.
		- Threat: Number of coins that can be killed by any opponent in one die roll.
