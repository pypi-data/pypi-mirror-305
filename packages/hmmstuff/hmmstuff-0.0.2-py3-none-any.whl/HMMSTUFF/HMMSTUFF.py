import multiprocessing
import random
import math,pickle,sklearn,os
import numpy as np
from pomegranate import DiscreteDistribution,State,HiddenMarkovModel
from HMMSTUFF import structure_generation
SEED = 42
random.seed(SEED)
WORKING_DIR = "/".join(os.path.realpath(__file__).split("/")[:-1])+"/"

class hmm_model:
    def __init__(self,input,annot,sequence_only=False,name="noname"):

        self.hash = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19, "X":20}
        self.missing = self.hash["X"]

        self.annotationCDR = annot
        self.template_sequence = input.strip("-")
        self.pssm = None
        self.name = name
        self.model = self.build_hmm(self.template_sequence,self.annotationCDR)


    def define_probability_distribution(self,pos):
        #print("to do! fit this distro")
        missing_prob = 0.5
        if self.pssm is None:
            probs= [0.01]*21
            probs[self.hash[self.template_sequence[pos]]] = 0.8
            probs[self.missing] = missing_prob
        else:
            probs = [0.0]*21
            for aa in self.hash.keys():

                if aa=="X":
                    probs[self.hash[aa]] = missing_prob
                else:
                    probs[self.hash[aa]] = self.pssm[pos][aa]

        return DiscreteDistribution({k:probs[k] for k in range(len(probs))})

    def define_GAP_probability_distribution(self,pos):
        #print("to do! fit this distro")
        probs= [0.05]*21
        return DiscreteDistribution({k:probs[k] for k in range(len(probs))})

    #def define_INS_probability_distribution

    def build_hmm(self, seq,annot,verbose=False):
        names= []
        pos = 0
        distroGap = self.define_GAP_probability_distribution(0)
        names += ["D_start","D_end","I_start","I_end"]

        states = [State(distroGap,name = "D_start"),State(distroGap,name = "D_end"),State(None,name = "I_start"),State("I_end",name = "I_end")]
        for k,s in enumerate(seq):
            if annot[k]=="0":
                names+=["M_"+str(k)]
                distro = self.define_probability_distribution(k)
                states += [State(distro,name= names[-1])]
            elif annot[k]=="-":
                distro = self.define_GAP_probability_distribution(pos)
                names+=["D_hole_"+str(k)]

                states += [State(distro,name = names[-1])]
            elif annot[k] == "1":
                distro = None#self.define_INS_probability_distribution(pos)
                names += ["I_" + str(k)]

                states += [State(distro,name = names[-1])]

                distro = self.define_probability_distribution(k)
                names += ["M_" + str(k)]
                states += [State(distro,name = names[-1])]

                distro = self.define_GAP_probability_distribution(pos)
                names+=["D_"+str(k)]
                states += [State(distro,name = names[-1])]
            else:
                asd

        model = HiddenMarkovModel('gapped_model')
        model.add_states(states)


        hashing_names = {names[k]:k for k in range(len(names))}
        ### initial probs ###

        model.add_transition(model.start, states[hashing_names["D_start"]], 0.95)
        model.add_transition(model.start, states[hashing_names["M_0"]], 0.05)

        # initial gaps D ###

        model.add_transition(states[hashing_names["D_start"]], states[hashing_names["D_start"]], 0.95)
        model.add_transition(states[hashing_names["D_start"]], states[hashing_names["M_0"]], 0.05)

        #####################
        for k in range(len(seq)-1):
            if annot[k]=="0":

                if annot[k+1] == "0":
                    starting_state = "M_"+str(k)
                    ending_state ="M_"+str(k+1)
                    prob = 1.0
                    if verbose:
                        print("adding edge ", starting_state,ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)

                elif annot[k+1] == "-":
                    starting_state = "M_"+str(k)
                    ending_state ="D_hole_"+str(k+1)
                    prob = 1.0
                    if verbose:
                        print("adding edge ", starting_state,ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)
                elif annot[k+1] == "1":
                    starting_state = "M_"+str(k)
                    ending_state ="M_"+str(k+1)
                    prob = 0.9
                    if verbose:
                        print("adding edge ", starting_state,ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)
                    starting_state = "M_"+str(k)
                    ending_state ="D_"+str(k+1)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state,ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)

                    starting_state = "M_"+str(k)
                    ending_state ="I_"+str(k+1)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state,ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)
                else:
                    asd
            elif annot[k]=="-":
                if annot[k + 1] == "0":
                    starting_state = "D_hole_"+str(k)
                    ending_state = "D_hole_"+str(k)
                    prob = 0.8
                    if verbose:
                        print("adding edge ", starting_state,ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)
                    starting_state = "D_hole_"+str(k)
                    ending_state = "M_"+str(k+1)
                    prob = 0.2
                    if verbose:
                        print("adding edge ", starting_state,ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)
                elif annot[k + 1] == "1":

                    starting_state = "D_hole_" + str(k)
                    ending_state = "M_" + str(k + 1)
                    prob = 0.9
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]

                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)

                    starting_state = "D_hole_" + str(k)
                    ending_state = "D_hole_" + str(k)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]

                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)

                    starting_state = "D_hole_" + str(k)
                    ending_state = "I_" + str(k + 1)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)
            elif annot[k] == "1":
                if annot[k + 1] == "0":
                    starting_state = "M_" + str(k)
                    ending_state = "M_" + str(k + 1)
                    prob = 0.9
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)

                    starting_state = "D_" + str(k)
                    ending_state = "M_" + str(k + 1)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]

                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)

                    starting_state = "I_" + str(k)
                    ending_state = "M_" + str(k + 1)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]], prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)
                if annot[k + 1] == "-":
                    starting_state = "M_" + str(k)
                    ending_state = "D_hole_" + str(k + 1)
                    prob = 0.9
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]

                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)


                    starting_state = "D_" + str(k)
                    ending_state = "D_hole_" + str(k+1)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)
                    starting_state = "I_" + str(k)
                    ending_state = "D_hole_" + str(k + 1)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [[distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)
                if annot[k + 1] == "1":
                    ### M ###
                    starting_state = "M_" + str(k)
                    ending_state = "M_" + str(k + 1)
                    prob = 0.9
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)
                    starting_state = "M_" + str(k)
                    ending_state = "D_" + str(k + 1)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]

                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)
                    starting_state = "M_" + str(k)
                    ending_state = "I_" + str(k + 1)
                    prob = 0.05
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)
                    ##################
                    ####     I     ###
                    starting_state = "I_" + str(k)
                    ending_state = "M_" + str(k + 1)
                    prob = 0.45
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)

                    starting_state = "I_" + str(k)
                    ending_state = "I_" + str(k + 1)
                    prob = 0.45
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)

                    starting_state = "I_" + str(k)
                    ending_state = "D_" + str(k + 1)
                    prob = 0.1
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)
                    ##################
                    ####     D     ###
                    starting_state = "D_" + str(k)
                    ending_state = "D_" + str(k)
                    prob = 0.9
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)

                    starting_state = "D_" + str(k)
                    ending_state = "M_" + str(k)
                    prob = 0.1
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]

                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)

                    starting_state = "D_" + str(k)
                    ending_state = "I_" + str(k)
                    prob = 0.1
                    if verbose:
                        print("adding edge ", starting_state, ending_state)
                    #edge_matrix += [
                    #    [distributions[hashing_names[starting_state]], distributions[hashing_names[ending_state]],
                    #     prob]]
                    model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]],prob)



            else:
                asd

        final_position = len(annot)-1
        if annot[-1]=="0":

            starting_state = "M_" + str(final_position)
            ending_state = "D_end"
            prob = 0.95
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)

            starting_state = "M_" + str(final_position)
            prob = 0.05
            if verbose:
                print("adding edge ", starting_state, "END")
            model.add_transition(states[hashing_names[starting_state]], model.end, prob)

            starting_state = "D_end"
            ending_state = "D_end"
            prob = 0.95
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)

            starting_state = "D_end"
            ending_state = "END"
            prob = 0.05
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], model.end, prob)

        elif annot[-1]=="1":

            ## match to end ##
            starting_state = "M_" + str(final_position)
            ending_state = "D_end"
            prob = 0.95
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)

            starting_state = "M_" + str(final_position)
            ending_state = "END"
            prob = 0.05
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], model.end, prob)

            ## D to end ##

            ## match to end ##
            starting_state = "D_" + str(final_position)
            ending_state = "D_end"
            prob = 0.95
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)

            starting_state = "D_" + str(final_position)
            ending_state = "END"
            prob = 0.05
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], model.end, prob)

            ## I to end ##

            ## match to end ##
            starting_state = "I_" + str(final_position)
            ending_state = "D_end"
            prob = 0.95
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)

            starting_state = "I_" + str(final_position)
            ending_state = "END"
            prob = 0.05
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], model.end, prob)

            #final gaps

            starting_state = "D_end"
            ending_state = "D_end"
            prob = 0.95
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], states[hashing_names[ending_state]], prob)

            starting_state = "D_end"
            ending_state = "END"
            prob = 0.05
            if verbose:
                print("adding edge ", starting_state, ending_state)
            model.add_transition(states[hashing_names[starting_state]], model.end, prob)
        else:
            brokenstuff

        model.bake()
        #self.model = SparseHMM(distributions, edges=edge_matrix, starts=starts, ends=ends, max_iter=200,inertia=0.8, verbose=True)
        #state_names = hashing_names
        return model

    def encode_sequence(self,sequence):
        if "-" in sequence:
            raise ValueError("the testing sequence is supposed to be ungapped")
        sequence=sequence.replace("B","X").replace("Z","X")
        return [[self.hash[sequence[k]] for k in range(len(sequence))]]

    def select_sequences(self,sequences,threshold,verbose=True):
        ids = list(sequences.keys())
        scores = [self.score_sequence(sequences[seqID],scale_output=False) for seqID in ids]

        indices = [i for i, _ in sorted((i, x) for i, x in enumerate(scores) if not math.isnan(x))[-int(len(scores) * threshold):]]
        #indices = [i for i in scores if ((not math.isnan(i)) and (i>-480)) ]
        sel = {ids[k]: sequences[ids[k]] for k in indices}

        if verbose:
            print("selected ",len(sel),"over",len(sequences))

        return sel
    def fit(self,sequences,threshold=[0.3,0.2,0.1]):

        for iter in range(len(threshold)):
            selected = self.select_sequences(sequences,threshold=threshold[iter])
            encoded_seq = [self.encode_sequence(selected[sequenceID])[0] for sequenceID in selected.keys()]

            self.model.fit(encoded_seq,inertia=0.9,edge_inertia=0.9,verbose=True,n_jobs=multiprocessing.cpu_count(),stop_threshold=50)

    def fit_scaler(self,sequences):
        score = []
        for i in sequences.keys():
            score+=[self.score_sequence(sequences[i],scale_output=False)]

        self.scaler = sklearn.preprocessing.QuantileTransformer( n_quantiles=100, output_distribution='uniform',
                                                  ignore_implicit_zeros=False, subsample=10000, random_state=SEED,
                                                  copy=True)
        self.scaler.fit(np.array(score).reshape(-1,1))

    def align(self,sequence):
        encoded_seq = self.encode_sequence(sequence)[0]

        prob, y_hat = self.model.viterbi(encoded_seq)
        if prob==-float("inf"):
            return False

        states = [y_hat[k][1].name for k in range(len(y_hat))][1:-1]

        al_template,al_seq = align_sequencesFromStates(states,template_sequence=self.template_sequence.replace("-",""),sequence=sequence)

        return al_seq,al_template

    def probability(self,sequence):
        encoded_seq = self.encode_sequence(sequence)[0]
        return float(self.model.log_probability(encoded_seq))
    def score_sequence(self,sequence,iterations=300,scale_output=True):

        score = self.probability(sequence)#/len(sequence)

        random_scores=[]
        #return score
        for i in range(iterations):
            l = list(sequence)
            random.shuffle(l)
            random_sequence = "".join(l)
            random_scores+=[self.probability(random_sequence)]

        score = score - np.mean(random_scores)

        if scale_output:
            return float(self.scaler.transform([[score]])[0][0])
        else:
            return score



def align_sequencesFromStates(states, sequence, template_sequence):
    aligned_sequence = []
    aligned_template = []
    seq_index = 0
    template_index = 0

    for state in states:
        if state.startswith('M'):
            if seq_index < len(sequence) and template_index < len(template_sequence):
                aligned_sequence.append(sequence[seq_index])
                aligned_template.append(template_sequence[template_index])
                seq_index += 1
                template_index += 1
            else:
                break

        elif state.startswith('I'):
            if template_index < len(template_sequence):
                aligned_sequence.append('*')  # Gap in the sequence
                aligned_template.append(template_sequence[template_index])
                template_index += 1
            else:
                break

        elif (state.startswith('D_hole') or state.startswith('D_start') or state.startswith('D_end')):
            if seq_index < len(sequence):
                aligned_sequence.append(sequence[seq_index])
                aligned_template.append('-')
                seq_index += 1
            else:
                break
        elif state.startswith('D') and not (state.startswith('D_hole') or state.startswith('D_start') or state.startswith('D_end')):
            if seq_index < len(sequence):
                aligned_sequence.append(sequence[seq_index])
                aligned_template.append('*')
                seq_index += 1
            else:
                break

    aligned_sequence_str = ''.join(aligned_sequence)
    aligned_template_str = ''.join(aligned_template)

    return aligned_template_str, aligned_sequence_str

class HMMSTUFF:
    def __init__(self):
        self.models = {}
        self.load()

    def load(self,modelsFolder=WORKING_DIR+"models/"):

        for template in os.listdir(modelsFolder):
            model_name = template.replace(".m","")
            annotationCDR = pickle.load(open(modelsFolder+model_name+"/annotationCDR.m","rb"))
            template_sequence = pickle.load(open(modelsFolder+model_name+"/template_sequence.m","rb"))
            model = hmm_model(template_sequence, annotationCDR)
            model.model = pickle.load(open(modelsFolder+model_name+"/model.m","rb"))
            model.scaler = pickle.load(open(modelsFolder+model_name+"/scaler.m","rb"))
            self.models[model_name] = model

        return True

    def get_all_scores(self,sequence):
        tot_score = []
        for modelID in sorted(list(self.models.keys())):

            score = round(self.models[modelID].score_sequence(sequence), 2)
            if score == False:
                tot_score += [0.0]
            else:
                tot_score += [score]
        return tot_score

    def get_all_sequences_scores(self,sequences,ncpus=multiprocessing.cpu_count()):
        seq_ids = list(sequences.keys())
        sequences_input = [sequences[k] for k in seq_ids]
        final = {}

        if ncpus>1:
            print("running multicore")
            args = []
            for k in range(len(seq_ids)):
                args += [(sequences_input[k],)]

            with multiprocessing.Pool(processes=ncpus) as pool:

                res = pool.starmap(self.get_all_scores,args)

            for k in range(len(seq_ids)):
                final[seq_ids[k]] = res[k]
        else:
            print("running single core")
            for k in range(len(seq_ids)):
                print("starting",seq_ids[k])
                final[seq_ids[k]] = self.get_all_scores(sequences_input[k])

        return final
    def get_template(self,sequence):
        results = {}
        best_score = None
        best_doable = False
        best_template = None
        best_temSubstring = None
        best_seqSubstring = None
        for modelID in self.models.keys():

            out = self.models[modelID].align(sequence)
            if out !=False:
                al, al_template = out
                score = round(self.models[modelID].score_sequence(sequence), 2)
            else:
                al, al_template = (False,False)
            if out != False:
                al, al_template = out
                max([(i, i + len(sub)) for i, sub in enumerate(al) if
                     '-' not in sub and '*' not in sub and '-' not in al_template[
                                                                      i:i + len(sub)] and '*' not in al_template[
                                                                                                     i:i + len(sub)]],
                    key=lambda x: x[1] - x[0])

                matches = []
                for i in range(len(al)):
                    if al[i] not in "*" and al_template[i] not in "*":
                        start = i
                        while i < len(al) and al[i] not in "*" and al_template[i] not in "*":
                            i += 1
                        end = i
                        matches.append((start, end))

                start, end = max(matches, key=lambda x: x[1] - x[0])

                seqSubstring = al[start:end]
                temSubstring = al_template[start:end]

                seqSubstring = "".join([seqSubstring[i] for i in range(len(temSubstring)) if temSubstring[i] != "-"])
                temSubstring = temSubstring.replace("-","")

                m = [temSubstring[k]==seqSubstring[k] for k in range(len(seqSubstring))]
                seq_id = round(sum(m)/len(temSubstring), 2)
                coverage = round(len(seqSubstring)/len(al_template.replace("-","").replace("*","")), 2)

                nonduable = (coverage < 0.8) or (score<0.5)

            if out == False:
                score = "BAD"
                doable = False
                temSubstring = None
                seqSubstring = None
            elif nonduable:
                score = score
                doable = False
                temSubstring = None
                seqSubstring = None
            else:

                # print(test_sequence_id,"score:",score,"seq id alignment:", round(sum(matches)/len(matches),2))
                doable = True

            if score=="BAD":
                pass
            elif best_score is None and best_doable==False and score!="BAD":

                best_score = score
                best_doable = doable
                best_template = modelID
                if doable:
                    best_temSubstring = temSubstring
                    best_seqSubstring = seqSubstring

            elif (best_score is not None) and not best_doable:
                # not duable best template

                if doable:
                    best_score = score
                    best_doable = doable
                    best_template = modelID
                    best_temSubstring = temSubstring
                    best_seqSubstring = seqSubstring

                elif best_score < score:
                    best_score = score
                    best_template = modelID

                else:
                    pass

            elif (best_score is not None) and  best_doable:
                # duable best template

                if doable and best_score < score:
                    best_score = score
                    best_doable = doable
                    best_template = modelID
                    best_temSubstring = temSubstring
                    best_seqSubstring = seqSubstring

                else:
                    pass

            results[modelID] = {}
            results[modelID]["alignment"] = (al,al_template)
            results[modelID]["substrings"] = (best_seqSubstring, best_temSubstring)
            results[modelID]["template_sequence"] = self.models[modelID].template_sequence.replace("-", "")
            results[modelID]["score"] = score
            results[modelID]["doable"] = doable
            results[modelID]["best_template_name"] = modelID

        if best_template is not None:
            return results[best_template]
        else:
            results = {}
            results["alignment"] = False
            results["substrings"] = False
            results["template_sequence"] = False
            results["score"] = False
            results["doable"] = False
            results["best_template_name"] = None
            return results

    def predict_structure(self,sequence,name,template_folder = WORKING_DIR+"/templates/",outfile = "outpdb.pdb",tmp_folder=os.getcwd()+"/foldX_tmp/",foldx_bin="foldx" ):
        template = self.get_template(sequence)
        results = {}

        if template["best_template_name"] is None:
            print("No template available for "+name+"! No similar LC amyloid structure is known")
            template["energy"] = None
            template["pdb_file"] = None
            return template

        elif not template["doable"]:
            print("The best template for  "+name+" is ",template["best_template_name"], "but it is not good enough to make the structure")
            template["energy"] = None
            template["pdb_file"] = None
            return template
        else:
            print("The best template for "+name+" is ",template["best_template_name"], "running structural prediction, it might take some time...")
            alignmentSeq,alignmentTem = template["substrings"]

            templatePDB = template_folder+template["best_template_name"]+".pdb"
            energy = structure_generation.predict_structure(alignmentSeq,alignmentTem,template["template_sequence"].replace("-",""),templatePDB, outFile=outfile ,tmp_folder=tmp_folder,foldx_bin=foldx_bin)

            template["energy"] = energy
            template["pdb_file"] = outfile

            return template

    def evaluate_sequence(self, sequence,name):
        template = self.get_template(sequence)
        results = {}

        if template["best_template_name"] is None:
            print("No template available for "+name+"! No similar LC amyloid structure is known")

            return template

        elif not template["doable"]:
            print("The best template for "+name+" is ",template["best_template_name"], "but it is not good enough to make the structure due to gaps in the alignment")

            return template
        else:
            print("The best template for "+name+" is ",template["best_template_name"])

            return template

    def evaluate_sequences(self,sequences,ncpus=multiprocessing.cpu_count()):
        seq_ids = list(sequences.keys())
        sequences_input = [sequences[k] for k in seq_ids]
        final = {}

        if ncpus>1:
            args = []
            for k in range(len(seq_ids)):
                args += [(sequences_input[k],seq_ids[k])]

            with multiprocessing.Pool(processes=ncpus) as pool:

                res = pool.starmap(self.evaluate_sequence,args)

            for k in range(len(seq_ids)):
                final[seq_ids[k]] = res[k]
        else:
            for k in range(len(seq_ids)):
                final[seq_ids[k]] = self.evaluate_sequence(sequences_input[k],seq_ids[k])

        return final
    def predict_structures(self,sequences, template_folder = WORKING_DIR+"/templates/", folder_out_pdbs = os.getcwd()+"/PDB_out/",ncpus = multiprocessing.cpu_count(),tmp_folder=os.getcwd()+"/foldX_tmp/",foldx_bin="foldx" ):
        seq_ids = list(sequences.keys())
        sequences_input = [sequences[k] for k in seq_ids]
        final = {}

        if not os.path.exists(folder_out_pdbs):
            os.makedirs(folder_out_pdbs)
        ncpus = 1
        if ncpus>1:
            print("Running structure prediction in multicore...")
            args = []
            for k in range(len(seq_ids)):
                args += [(sequences_input[k],
                          seq_ids[k],
                          template_folder,
                          folder_out_pdbs+seq_ids[k]+".pdb",
                          tmp_folder,
                          foldx_bin)]

            with multiprocessing.Pool(processes=ncpus) as pool:

                res = pool.starmap(self.predict_structure,args)

            for k in range(len(seq_ids)):
                final[seq_ids[k]] = res[k]
        else:
            print("Running structure prediction in single core...")
            for k in range(len(seq_ids)):
                final[seq_ids[k]] = self.predict_structure(sequences_input[k],seq_ids[k], template_folder, folder_out_pdbs+seq_ids[k]+".pdb", tmp_folder,foldx_bin)

        return final


