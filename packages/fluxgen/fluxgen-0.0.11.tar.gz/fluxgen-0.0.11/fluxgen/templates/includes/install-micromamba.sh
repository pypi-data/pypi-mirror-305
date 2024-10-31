# Dependencies - specifically let's install micromamba for flux
which micromamba || (
  apt-get update && apt-get install -y bzip2 curl || (yum update -y && yum install -y bzip2 curl)

  # Install to root bin
  curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj ./micromamba
  mv ./micromamba /usr/local/bin/micromamba
)
