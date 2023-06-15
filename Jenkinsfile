pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'Tests', url: 'https://github.com/DenkingOfficial/mlops_hw_6.git'
            }
        }
        stage('Install requirements') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage('Downloading data') {
            steps { 
                sh 'python ./scripts/download_data.py'
            }
        }
        stage('Data preparation') {
            steps {
                sh 'python ./scripts/dataset_preprocess.py'
            }
        }
        stage('Data quality testing') {
            steps {
                sh 'python -m pytest ./tests/test_dataset.py'
            }
        }
        stage('Model training') {
            steps {
                sh 'python ./scripts/model_train.py'
            }
        }
        stage('Model testing') {
            steps {
                sh 'python ./scripts/model_testing.py'
            }
        }
        stage('Model unit tests') {
            steps {
                sh 'python -m pytest ./tests/test_model.py'
            }
        }
        stage('Webui test') {
            steps {
                sh 'python app.py &'
                sh 'sleep 10s'
                sh 'python -m pytest ./tests/test_webui.py'
                sh 'pkill -f app.py'
            }
        }
    }
}