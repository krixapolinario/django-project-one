node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube analysis') {
    def scannerHome = tool 'sonar-scanner-3.2';
    withSonarQubeEnv('sonar-watcher') {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}