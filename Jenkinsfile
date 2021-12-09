pipeline {
    agent any

    stages {
        stage('execute python') { 
            steps {
                sh 'pip install json2html; python3 file.py'
            }
        }
    }
}
