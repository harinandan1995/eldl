import argparse
import matplotlib.pyplot as plt



def main():

    parser = argparse.ArgumentParser(description='Pie Generator. Generates only SVG images.')
    parser.add_argument('-c','--colors',help='List of colors(hexcode without \'#\') for the pie.',nargs='+',required=True)
    parser.add_argument('-o','--out',help='Outfile path.',required=True)

    args = parser.parse_args()

    colors = ['#'+col for col in args.colors]
    colen = len(colors)
    weights = [1.0/colen]*colen

    plt.figure(figsize=[4,4])
    plt.pie(weights,colors=colors,startangle=90)
    plt.savefig(args.out,transparent=True,format='jpg',wedgeprops={'linewidth': 100})

    print('Pie Created!')
    return

if __name__ == '__main__':
    main()