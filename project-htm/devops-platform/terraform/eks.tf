module "eks" {
  source = "terraform-aws-modules/eks/aws"

  cluster_name    = "devops-cluster"
  cluster_version = "1.29"

  vpc_id  = module.vpc.vpc_id
  subnets = module.vpc.private_subnets

  eks_managed_node_groups = {
    default = {
      desired_size   = 1
      max_size       = 1
      min_size       = 1

      instance_types = ["t3.small"]
    }
  }
}