pipeline {
    agent any
    
    environment {
        DOCKERHUB_USERNAME = credentials('dockerhub-credentials')
    }
    
    stages {
        stage('Select Version') {
            steps {
                script {
                    def versionChoices = ['*/main', 'refs/tags/dataset_v2', 'refs/tags/dataset_merged']
                    selectedVersion = input message: 'Choose a dataset version:',
                                       parameters: [choice(name: 'version', choices: versionChoices.join('\n'), description: 'Select a version from the list')]
                    echo "Selected dataset version: ${selectedVersion}"
                }
            }
        }
        stage('Clone Repo') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: selectedVersion]],
                    userRemoteConfigs: [[url: 'https://github.com/DenkingOfficial/mlops_hw_6.git']]
                ])
            }
        }
        stage('Install requirements') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage('Downloading data') {
            steps { 
                sh 'dvc pull'
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
                sh 'python -m pytest ./tests/test_model.py'
            }
        }
        stage('Docker build') {
            steps {
                sh 'sudo docker build -t denking/text_tonality_classifier:1.0 .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                        sh 'docker logout'
                        sh "docker login -u '${DOCKERHUB_USERNAME}' -p '${DOCKERHUB_PASSWORD}' docker.io"
                        sh 'docker push denking/text_tonality_classifier:1.0'
                        sh 'docker logout'
                    }
                }
            }
        }
        stage('Docker run') {
            steps {
                sh 'sudo docker run -d -p 7860:7860 denking/text_tonality_classifier:1.0'
                sh 'sleep 10s'
            }
        }
        stage('Webui test') {
            steps {
                sh 'python -m pytest ./tests/test_webui.py'
            }
        }
    }
}
