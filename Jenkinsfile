        node{
        
        stage "build" 
            sh "mkdir -p test"
            
            sh "pwd"
            
        stage "Checkout"
        
            checkout([$class: 'GitSCM', branches: [[name: '*/master']],
            userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd.git'], [credentialsId: 'vamsi']]])
        }
    