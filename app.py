import streamlit as st
import random

# Initialize the task list and task index in session state
if 'task_index' not in st.session_state:
    st.session_state.task_index = 0
    st.session_state.tasks = ['apply', 'random_word', 'interview']
    st.session_state.words = [
    "Two Sum",
    "Best Time to Buy and Sell Stock",
    "Contains Duplicate",
    "Product of Array Except Self",
    "Maximum Subarray",
    "Maximum Product Subarray",
    "Find Minimum in Rotated Sorted Array",
    "Search in Rotated Sorted Array",
    "3 Sum",
    "Container With Most Water",
    "Sum of Two Integers",
    "Number of 1 Bits",
    "Counting Bits",
    "Missing Number",
    "Reverse Bits",
    "Climbing Stairs",
    "Coin Change",
    "Longest Increasing Subsequence",
    "Longest Common Subsequence",
    "Word Break Problem",
    "Combination Sum",
    "House Robber",
    "House Robber II",
    "Decode Ways",
    "Unique Paths",
    "Jump Game",
    "Clone Graph",
    "Course Schedule",
    "Pacific Atlantic Water Flow",
    "Number of Islands",
    "Longest Consecutive Sequence",
    "Insert Interval",
    "Merge Intervals",
    "Non-overlapping Intervals",
    "Reverse a Linked List",
    "Detect Cycle in a Linked List",
    "Merge Two Sorted Lists",
    "Merge K Sorted Lists",
    "Remove Nth Node From End Of List",
    "Reorder List",
    "Set Matrix Zeroes",
    "Spiral Matrix",
    "Rotate Image",
    "Word Search",
    "Longest Substring Without Repeating Characters",
    "Longest Repeating Character Replacement",
    "Minimum Window Substring",
    "Valid Anagram",
    "Group Anagrams",
    "Valid Parentheses",
    "Valid Palindrome",
    "Longest Palindromic Substring",
    "Palindromic Substrings",
    "Maximum Depth of Binary Tree",
    "Same Tree",
    "Invert/Flip Binary Tree",
    "Binary Tree Maximum Path Sum",
    "Binary Tree Level Order Traversal",
    "Serialize and Deserialize Binary Tree",
    "Subtree of Another Tree",
    "Construct Binary Tree from Preorder and Inorder Traversal",
    "Validate Binary Search Tree",
    "Kth Smallest Element in a BST",
    "Lowest Common Ancestor of BST",
    "Implement Trie (Prefix Tree)",
    "Add and Search Word",
    "Word Search II",
    "Merge K Sorted Lists",
    "Top K Frequent Elements",
    "Find Median from Data Stream"
]
    st.session_state.questions = [
    "What is the difference between supervised and unsupervised learning?",
    "Explain the bias-variance tradeoff.",
    "What is a confusion matrix, and why is it useful?",
    "Describe the process of cross-validation.",
    "How do you handle missing data in a dataset?",
    "What is the purpose of regularization in machine learning models?",
    "Explain the concept of overfitting and underfitting.",
    "What is the difference between L1 and L2 regularization?",
    "Describe the k-nearest neighbors (KNN) algorithm.",
    "What is the purpose of a ROC curve?",
    "Explain the difference between precision and recall.",
    "What is a support vector machine (SVM)?",
    "Describe the Naive Bayes classifier and its assumptions.",
    "What is a decision tree, and how does it work?",
    "Explain the concept of ensemble learning.",
    "What is the difference between bagging and boosting?",
    "Describe the random forest algorithm.",
    "What is gradient boosting?",
    "Explain the k-means clustering algorithm.",
    "What is hierarchical clustering?",
    "Describe the principle of dimensionality reduction.",
    "What is principal component analysis (PCA)?",
    "Explain the t-SNE algorithm.",
    "What is the curse of dimensionality?",
    "Describe the difference between generative and discriminative models.",
    "What is a neural network?",
    "Explain the concept of backpropagation in neural networks.",
    "What is a convolutional neural network (CNN)?",
    "Describe the architecture of a recurrent neural network (RNN).",
    "What is long short-term memory (LSTM)?",
    "Explain the concept of an autoencoder.",
    "What is a generative adversarial network (GAN)?",
    "Describe the use of transfer learning in deep learning.",
    "What is the difference between a hyperparameter and a parameter?",
    "Explain the purpose of a learning rate in training neural networks.",
    "What is dropout, and how does it help in training neural networks?",
    "Describe the difference between batch gradient descent and stochastic gradient descent.",
    "What are word embeddings, and why are they useful?",
    "Explain the concept of attention mechanisms in neural networks.",
    "What is reinforcement learning?",
    "Describe the Q-learning algorithm.",
    "What is a Markov decision process (MDP)?",
    "Explain the concept of a policy in reinforcement learning.",
    "What is the Bellman equation?",
    "Describe the exploration-exploitation tradeoff in reinforcement learning.",
    "What are some common activation functions used in neural networks?",
    "Explain the concept of a loss function in machine learning.",
    "What is the purpose of the softmax function?",
    "Describe the difference between logistic regression and linear regression.",
    "What is the F1 score, and how is it calculated?"
]


# Function to display the next task
def next_task():
    st.session_state.task_index = (st.session_state.task_index + 1) % len(st.session_state.tasks)

# Streamlit app layout
st.title('Task Display App')
st.write('Click the button to display the next task in order.')

# Display the current task
current_task = st.session_state.tasks[st.session_state.task_index]

if current_task == 'random_word':
    current_task = random.choice(st.session_state.words) 

if current_task == 'interview':
    current_task = random.choice(st.session_state.questions) 
st.header(current_task)

# Button to go to the next task
if st.button('Next Task'):
    next_task()

