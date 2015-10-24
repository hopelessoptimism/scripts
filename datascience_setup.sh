## Setup a data science development mac mini box

# ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
# also need to install Anaconda distribution

## Mac apps
brew tap phinze/cask
brew install brew-cask
brew cask install google-chrome
brew cask install firefox
brew cask install mou
brew cask install iterm2
brew cask install xquartz
brew cask install virtualbox
brew cask install vagrant
brew cask install sublime-text
brew cask install pgadmin3

## mac packages
brew install wget
brew install postgres
brew install mongodb
brew install graphviz
brew install imagemagick

cd /Applications
wget https://justgetflux.com/mac/Flux.zip
unzip Flux.zip
rm Flux.zip

# python
# curl -L http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-1.8.0-MacOSX-x86_64.sh | sh
conda install --yes statsmodels
conda install --yes networkx
pip install pymc
pip install pymongo

# R
brew update
brew tap homebrew/science
brew install gfortran r
