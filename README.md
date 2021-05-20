# Azure-DevOps

Watch this space, "iyanu mashele" in Azure DevOps-NanoDegree

[![CI](https://github.com/samuelarogbonlo/Azure-DevOps/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/samuelarogbonlo/Azure-DevOps/actions/workflows/main.yml)

## Azure-CLI

The most important word in using the Azure CLI is "az", it is used to perform several operation on the Axure platform. 

You can use this from the azure shell and the machine terminal as well; personally, I prefer the terminal but I have to first login with ```az login``` which redirects you to your browser for authentication before you go ahead with operation commands

### Basic Commands To Provision A virtual Machine

- ```az account list``` to show all the metadata about the account you are utilizing
- ```az group create --location eastus2 --name myRG``` to create a resource group and set it in a location with any preffered name.
- ```az vm create -n DefaultVM -g mYRG --image UBUNTULTS --generate-ssh-keys``` to create a Linux VM that has Ubuntu as its operating system
- Go ahead and search your Virtual machine name on Azure dashboard
- ```ssh@machinename IP address``` to connect to the VM recently created from your terminal.
- Go ahead and play around with the VM
- After all this, you can delete the resource to shut down the VM so as to avoid incuring unnecessary cost. The command is ```az group delete -n mYRG```

There are a couple of other stuff that could be done here so I believe with time, we would address them. 
