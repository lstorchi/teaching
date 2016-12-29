import sys
sys.path.append("./common")
import mtestmod

def main ():
  values = [2, 4, 5.6, 7]
  print "adding ", mtestmod.scalar
  mtestmod.add_to_list(values)
  print values


if __name__ == "__main__":
  print "viene eseguito solo se main"
  main()
