import matplotlib.pyplot as plt


if __name__ == "__main__":
    #x: dim_input (n)
    dim=[5,10,25,50,100,250,500,1000]

    #y: time (t): (cycle/NOcycle)
        
        #y: time (t) cycle
    DFS_cycle = [0.01562037467956543, 0.015618228912353515, 0.015624876022338868, 0.01562283992767334, 0.016563045978546142, 0.01999977970123291, 0.02471842670440674, 0.051452561378479006]
    UFQuickUnion_cycle = [0.0, 0.015649080276489258, 0.03136491775512695, 0.20317864418029785, 0.6406698226928711, 3.781280279159546, 14.015471935272217, 92.42085814476013]
    UFQuickUnionBalanced_cycle = [0.015648365020751953, 0.015625, 0.03125262260437012, 0.1562213897705078, 0.6562447547912598, 3.5155885219573975, 13.531162738800049, 87.35833811759949]
    UFQuickFind_cycle = [0.015626907348632812, 0.015691757202148438, 0.04678988456726074, 0.14066839218139648, 0.5155961513519287, 3.078091621398926, 13.109158754348755, 66.01486849784851]
    UFQuickFindBalanced_cycle = [0.015626907348632812, 0.015691757202148438, 0.04678988456726074, 0.14066839218139648, 0.5155961513519287, 3.078091621398926, 13.109158754348755, 66.01486849784851]
    UFQuickUnionBalancedPathCompression_cycle = [0.015633106231689453, 0.015561103820800781, 0.04687094688415527, 0.0937643051147461, 0.5313243865966797, 3.312462568283081, 12.249871492385864, 54.726999282836914]
    UFQuickUnionBalancedPathSplitting_cycle = [0.015594959259033203, 0.015709400177001953, 0.0467686653137207, 0.1874847412109375, 0.6718826293945312, 3.9999582767486572, 18.702922821044922, 114.52999186515808]
    
        #y: time (t) NOcycle
    #DFS_withoutcycle = [0.024999666213989257, 0.0249997615814209, 0.027499656677246093, 0.026562318801879883, 0.027343425750732422, 0.02987466239929199, 0.030843364715576173, 0.036734040975570675]
    #UFQuickUnion_withoutcycle = [0.015596628189086914, 0.031248092651367188, 0.06250190734863281, 0.18752026557922363, 0.6718723773956299, 3.640585422515869, 15.734201431274414, 82.17096638679504]
    #UFQuickUnionBalanced_withoutcycle = [0.015626192092895508, 0.03125119209289551, 0.06249713897705078, 0.17189979553222656, 0.593775749206543, 3.5155866146087646, 15.484203815460205, 78.96497392654419]    
    #UFQuickFind_withoutcycle = [0.015622377395629883, 0.031280517578125, 0.04687166213989258, 0.1562204360961914, 0.5468676090240479, 3.203089475631714, 13.765474081039429, 67.98355770111084]
    #UFQuickFindBalanced_withoutcycle = [0.03124833106994629, 0.031217336654663086, 0.06250214576721191, 0.1249990463256836, 0.49999260902404785, 3.1405911445617676, 13.718598365783691, 65.84312272071838]
    #UFQuickUnionBalancedPathCompression_withoutcycle = [0.015625715255737305, 0.03125262260437012, 0.04690408706665039, 0.1405956745147705, 0.49996304512023926, 3.2655863761901855, 11.640526056289673, 55.04442286491394]
    #UFQuickUnionBalancedPathSplitting_withoutcycle = [0.031275272369384766, 0.03127884864807129, 0.04687690734863281, 0.1874990463256836, 0.7031166553497314, 4.0937089920043945, 21.577860593795776, 116.68628692626953]
    
    #CODE_plotting_for_cycle
    plt.plot(dim, DFS_cycle, 'green', label="DFS_cycle")
    plt.plot(dim, UFQuickUnion_cycle, 'red', label="UFQuickUnion_cycle")
    plt.plot(dim, UFQuickUnionBalanced_cycle, 'cyan', label="UFQuickUnionBalanced_cycle")
    plt.plot(dim, UFQuickFind_cycle, 'yellow', label="UFQuickFind_cycle")
    plt.plot(dim, UFQuickFindBalanced_cycle, 'pink', label="UFQuickFindBalanced_cycle")
    plt.plot(dim, UFQuickUnionBalancedPathCompression_cycle, 'orchid', label="UFQuickUnionBalancedPathCompression_cycle")
    plt.plot(dim, UFQuickUnionBalancedPathSplitting_cycle, 'black', label="UFQuickUnionBalancedPathSplitting_cycle")
    
    #CODE_plotting_for_NOcycle
    #plt.plot(dim, DFS_withoutcycle, 'green', label="DFS_withoutcycle")
    #plt.plot(dim, UFQuickUnion_withoutcycle, 'red', label="UFQuickUnion_withoutcycle")
    #plt.plot(dim, UFQuickUnionBalanced_withoutcycle, 'cyan', label="UFQuickUnionBalanced_withoutcycle")
    #plt.plot(dim, UFQuickFind_withoutcycle, 'yellow', label="UFQuickFind_withoutcycle")
    #plt.plot(dim, UFQuickFindBalanced_withoutcycle, 'pink', label="UFQuickFindBalanced_withoutcycle")
    #plt.plot(dim, UFQuickUnionBalancedPathCompression_withoutcycle, 'orchid', label="UFQuickUnionBalancedPathCompression_withoutcycle")
    #plt.plot(dim, UFQuickUnionBalancedPathSplitting_withoutcycle, 'black', label="UFQuickUnionBalancedPathSplitting_withoutcycle")

    plt.xlim(0, 1000)
    plt.ylim(0, 120)
    plt.xlabel('n: dimensione input')
    plt.ylabel('t: time')
    plt.title('[TEST GRAPH]')
    plt.legend(loc="upper left")
    plt.show()

