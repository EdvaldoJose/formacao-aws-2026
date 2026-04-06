git config --global alias.start '!f() { \
  git checkout developer && \
  git pull && \
  git switch -c feature/$1; \
}; f'