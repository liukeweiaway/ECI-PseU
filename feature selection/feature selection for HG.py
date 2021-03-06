#!/usr/bin/env python
# -*- coding:utf-8-*-
# auther:kewei Liu time:2019/3/3 16:26  QQ:422209303  e-mail:Liukeweiaway@hotmail.com
# --------------------------------------------------------------------------
file_input = 'H_200.txt'
file_out = open('H_200_dnc_psnp.txt', mode='a')


def nc(seq):
    seq_length = len(seq)
    A = round(seq.count('A') / seq_length, 3)
    U = round(seq.count('U') / seq_length, 3)
    C = round(seq.count('C') / seq_length, 3)
    G = round(seq.count('G') / seq_length, 3)
    return A, U, C, G


def dnc(seq):
    seq_length = len(seq)
    AA = round(seq.count('AA') / seq_length, 3)
    AU = round(seq.count('AU') / seq_length, 3)
    AC = round(seq.count('AC') / seq_length, 3)
    AG = round(seq.count('AG') / seq_length, 3)
    UA = round(seq.count('UA') / seq_length, 3)
    UU = round(seq.count('UU') / seq_length, 3)
    UC = round(seq.count('UC') / seq_length, 3)
    UG = round(seq.count('UG') / seq_length, 3)
    CA = round(seq.count('CA') / seq_length, 3)
    CU = round(seq.count('CU') / seq_length, 3)
    CC = round(seq.count('CC') / seq_length, 3)
    CG = round(seq.count('CG') / seq_length, 3)
    GA = round(seq.count('GA') / seq_length, 3)
    GU = round(seq.count('GU') / seq_length, 3)
    GC = round(seq.count('GC') / seq_length, 3)
    GG = round(seq.count('GG') / seq_length, 3)
    return AA, AU, AC, AG, UA, UU, UC, UG, CA, CU, CC, CG, GA, GU, GC, GG


def tnc(seq):
    seq_length = len(seq)
    first = ['A', 'U', 'C', 'G']
    second = ['A', 'U', 'C', 'G']
    third = ['A', 'U', 'C', 'G']
    tri_nucleotide_dict = {}
    tri_nucleotide_values = []
    for x in range(4):
        for y in range(4):
            for z in range(4):
                tri_nucleotide_XXX = first[x] + second[y] + third[z]
                tri_nucleotide_dict[tri_nucleotide_XXX] = 0
    for tri_nucleotide in tri_nucleotide_dict.keys():
        tri_nucleotide_dict[tri_nucleotide] = round(seq.count(tri_nucleotide) / seq_length, 3)
    for dict_value in tri_nucleotide_dict.values():
        tri_nucleotide_values.append(dict_value)
    return tri_nucleotide_values


def psnp(seq):
    seq_length = len(seq)
    PNlist = [[0.026, -0.056, -0.004, -0.024, -0.038, -0.004, -0.043, 0.008, -0.077, -0.105, 0.0, 0.103, -0.065, -0.024,
               -0.026, -0.028, -0.014, -0.062, -0.051, -0.054, -0.021],
              [-0.08, -0.01, -0.01, 0.006, 0.055, -0.081, -0.012, -0.053, -0.012, 0.074, 0.0, 0.087, 0.014, -0.059,
               -0.012, 0.021, -0.041, -0.037, -0.039, 0.002, 0.008],
              [0.006, 0.032, -0.016, 0.034, -0.004, 0.022, 0.049, 0.028, 0.01, -0.012, 0.0, -0.059, 0.089, 0.022, 0.016,
               -0.002, 0.049, 0.047, 0.041, 0.074, 0.032],
              [0.049, 0.035, 0.03, -0.016, -0.012, 0.063, 0.007, 0.017, 0.079, 0.042, 0.0, -0.132, -0.038, 0.061, 0.023,
               0.01, 0.006, 0.053, 0.049, -0.022, -0.021]]
    specific = [None] * seq_length
    for j in range(seq_length):
        if seq[j] == 'A':
            specific[j] = PNlist[0][j]
        elif seq[j] == 'U':
            specific[j] = PNlist[1][j]
        elif seq[j] == 'C':
            specific[j] = PNlist[2][j]
        elif seq[j] == 'G':
            specific[j] = PNlist[3][j]
    return specific


def psdp(seq):
    seq_length = len(seq)
    PDNlist = [
        [-0.002, -0.01, 0.016, -0.018, -0.02, -0.02, -0.02, -0.042, -0.048, 0.0, 0.0, 0.008, -0.038, -0.024, 0.002,
         -0.012, -0.006, -0.036, -0.032, -0.044],
        [-0.004, -0.032, 0.006, 0.008, -0.031, 0.008, -0.019, 0.0, -0.015, -0.105, 0.0, 0.03, -0.019, -0.02, 0.008,
         -0.024, -0.006, -0.022, -0.021, -0.008],
        [0.002, -0.027, -0.002, 0.0, -0.005, 0.0, -0.011, 0.022, 0.002, 0.0, 0.0, 0.057, -0.002, 0.018, -0.012, 0.022,
         -0.004, -0.004, 0.006, -0.006],
        [0.03, 0.012, -0.024, -0.014, 0.016, 0.008, 0.006, 0.028, -0.017, 0.0, 0.0, 0.008, -0.006, 0.002, -0.025,
         -0.014, 0.002, 0.0, -0.004, 0.004],
        [-0.022, -0.005, -0.039, 0.0, 0.004, -0.024, 0.019, 0.009, -0.027, 0.0, 0.103, 0.014, -0.01, -0.017, -0.016,
         -0.005, -0.031, -0.029, -0.004, 0.012],
        [-0.032, -0.004, 0.006, 0.028, -0.014, -0.02, -0.026, -0.024, -0.01, 0.074, 0.087, 0.014, -0.006, -0.028, 0.002,
         -0.024, -0.016, -0.032, -0.012, -0.002],
        [-0.013, -0.004, 0.025, -0.025, 0.021, -0.023, 0.002, -0.029, -0.021, 0.0, -0.059, 0.076, 0.014, -0.023, -0.008,
         0.031, -0.009, 0.01, -0.006, -0.002],
        [-0.014, 0.002, -0.002, 0.002, 0.044, -0.014, -0.006, -0.008, 0.044, 0.0, -0.132, -0.018, 0.016, 0.008, 0.01,
         0.018, 0.014, 0.014, -0.016, -0.006],
        [-0.037, 0.006, -0.016, -0.018, 0.012, -0.01, 0.008, -0.027, -0.019, 0.0, 0.0, -0.043, 0.04, -0.004, -0.02,
         -0.008, -0.024, 0.022, -0.01, 0.017],
        [0.004, 0.01, 0.002, 0.04, -0.025, -0.024, 0.008, 0.006, 0.018, -0.012, 0.0, -0.005, -0.008, 0.02, 0.002, 0.002,
         -0.006, -0.006, -0.002, 0.032],
        [0.025, -0.004, -0.022, 0.002, -0.002, 0.024, 0.022, 0.013, -0.006, 0.0, 0.0, -0.027, 0.014, -0.008, 0.021,
         -0.006, 0.047, 0.01, 0.029, 0.016],
        [0.014, 0.02, 0.02, 0.01, 0.01, 0.032, 0.01, 0.036, 0.016, 0.0, 0.0, 0.014, 0.042, 0.014, 0.014, 0.01, 0.032,
         0.02, 0.024, 0.01],
        [0.004, 0.004, 0.014, -0.002, 0.0, 0.012, 0.002, -0.017, -0.012, 0.0, 0.0, -0.045, -0.016, 0.018, 0.006, 0.01,
         -0.002, -0.008, -0.008, -0.004],
        [0.023, 0.016, -0.008, -0.023, -0.012, 0.025, -0.017, 0.006, 0.081, 0.042, 0.0, -0.027, -0.027, 0.016, 0.009,
         0.006, -0.008, 0.023, 0.037, -0.014],
        [0.019, 0.019, 0.035, 0.019, 0.008, 0.047, 0.015, 0.005, 0.012, 0.0, 0.0, -0.018, -0.004, 0.029, -0.002, 0.003,
         0.012, 0.025, 0.047, 0.025],
        [0.004, -0.004, -0.01, -0.01, -0.008, -0.02, 0.006, 0.022, -0.002, 0.0, 0.0, -0.043, 0.008, -0.002, 0.01,
         -0.009, 0.004, 0.014, -0.027, -0.028]]
    dspecific = [None] * (seq_length - 1)
    for j in range(seq_length - 1):
        if seq[j:j + 2] == 'AA':
            dspecific[j] = PDNlist[0][j]
        elif seq[j:j + 2] == 'AU':
            dspecific[j] = PDNlist[1][j]
        elif seq[j:j + 2] == 'AC':
            dspecific[j] = PDNlist[2][j]
        elif seq[j:j + 2] == 'AG':
            dspecific[j] = PDNlist[3][j]
        elif seq[j:j + 2] == 'UA':
            dspecific[j] = PDNlist[4][j]
        elif seq[j:j + 2] == 'UU':
            dspecific[j] = PDNlist[5][j]
        elif seq[j:j + 2] == 'UC':
            dspecific[j] = PDNlist[6][j]
        elif seq[j:j + 2] == 'UG':
            dspecific[j] = PDNlist[7][j]
        elif seq[j:j + 2] == 'CA':
            dspecific[j] = PDNlist[8][j]
        elif seq[j:j + 2] == 'CU':
            dspecific[j] = PDNlist[9][j]
        elif seq[j:j + 2] == 'CC':
            dspecific[j] = PDNlist[10][j]
        elif seq[j:j + 2] == 'CG':
            dspecific[j] = PDNlist[11][j]
        elif seq[j:j + 2] == 'GA':
            dspecific[j] = PDNlist[12][j]
        elif seq[j:j + 2] == 'GU':
            dspecific[j] = PDNlist[13][j]
        elif seq[j:j + 2] == 'GC':
            dspecific[j] = PDNlist[14][j]
        elif seq[j:j + 2] == 'GG':
            dspecific[j] = PDNlist[15][j]
    return dspecific


def pstp(seq):
    seq_length = len(seq)
    PDNlist = [[-0.002, 0.004, 0.008, -0.015, 0.0, -0.008, -0.012, -0.012, 0.0, 0.0, 0.0, -0.016, -0.01, -0.016, 0.002,
                0.0, -0.018, -0.024, -0.039],
               [0.009, 0.004, 0.041, -0.036, -0.004, -0.028, 0.0, -0.012, -0.097, 0.0, 0.0, 0.004, -0.024, 0.02, -0.008,
                -0.033,
                -0.004, -0.008, 0.004],
               [-0.012, -0.028, -0.012, -0.016, -0.008, 0.004, -0.008, -0.016, 0.0, 0.0, 0.0, 0.0, -0.024, -0.021,
                0.016, 0.004,
                -0.013, -0.008, 0.004],
               [0.004, -0.004, -0.012, 0.045, -0.029, 0.0, -0.009, -0.032, 0.0, 0.0, 0.0, 0.045, -0.008, -0.017, -0.008,
                0.004,
                0.041, -0.008, 0.004],
               [0.0, -0.041, 0.012, -0.024, -0.02, 0.016, -0.016, -0.004, 0.0, -0.057, 0.0, -0.012, -0.024, -0.02,
                -0.012, -0.016,
                -0.008, -0.02, 0.012],
               [0.0, -0.02, 0.024, -0.012, -0.02, 0.0, -0.004, -0.005, -0.028, 0.016, 0.0, 0.033, -0.008, -0.021,
                -0.008, -0.029,
                -0.012, -0.012, -0.053],
               [0.004, 0.004, 0.004, 0.008, -0.02, -0.012, -0.012, -0.004, 0.0, -0.073, 0.0, 0.029, -0.004, -0.024,
                0.037, -0.008,
                0.016, -0.004, 0.008],
               [-0.012, -0.009, -0.029, 0.045, 0.0, 0.012, -0.004, 0.012, 0.0, -0.097, 0.0, 0.012, 0.0, 0.024, 0.0,
                0.004, -0.008,
                -0.008, -0.008],
               [0.004, -0.008, -0.011, -0.02, -0.011, -0.017, -0.033, -0.023, 0.0, 0.0, 0.0, 0.018, -0.015, -0.025,
                0.002, -0.004,
                -0.017, -0.017, -0.041],
               [-0.008, -0.012, 0.014, 0.0, -0.004, -0.002, -0.006, 0.026, 0.002, 0.0, 0.0, -0.006, 0.008, 0.006,
                -0.008, 0.0,
                0.0, -0.008, 0.006],
               [-0.002, -0.008, 0.0, 0.004, 0.01, 0.01, 0.004, -0.002, 0.0, 0.0, 0.0, 0.022, -0.01, 0.018, -0.002, 0.01,
                -0.004,
                -0.006, 0.006],
               [0.006, 0.006, 0.002, 0.002, 0.0, 0.0, 0.012, 0.008, 0.0, 0.0, 0.0, 0.006, 0.004, 0.002, -0.002, 0.016,
                -0.002,
                0.002, -0.004],
               [0.01, 0.008, -0.012, -0.002, -0.002, 0.002, -0.004, -0.008, 0.0, 0.0, 0.0, -0.006, -0.008, -0.012,
                -0.004, -0.01,
                0.0, -0.008, -0.002],
               [0.012, -0.008, 0.0, 0.0, 0.0, 0.0, 0.002, 0.036, -0.017, 0.0, 0.0, 0.004, 0.004, 0.01, 0.0, -0.002,
                -0.002, 0.018,
                0.002],
               [-0.002, 0.016, -0.002, 0.004, 0.026, 0.008, -0.012, 0.002, 0.0, 0.0, 0.0, 0.002, 0.006, 0.004, -0.02,
                -0.008,
                0.004, 0.006, 0.004],
               [0.01, -0.004, -0.01, -0.016, -0.008, -0.002, 0.02, -0.002, 0.0, 0.0, 0.0, 0.008, -0.008, 0.0, 0.0,
                0.006, 0.0,
                -0.016, -0.008],
               [-0.018, 0.004, -0.018, 0.004, -0.008, -0.01, 0.0, -0.006, 0.0, 0.0, 0.008, 0.004, -0.012, -0.006,
                -0.012, -0.006,
                -0.004, -0.01, 0.0],
               [-0.016, 0.004, -0.033, -0.004, 0.02, -0.016, 0.012, 0.016, -0.052, 0.0, 0.061, -0.004, -0.025, 0.0,
                -0.033, 0.012,
                -0.024, -0.032, -0.02],
               [0.004, -0.004, 0.0, 0.012, -0.004, -0.004, 0.02, 0.012, 0.0, 0.0, 0.113, 0.012, 0.032, -0.008, 0.032,
                0.0, -0.008,
                -0.004, -0.004],
               [0.004, -0.016, -0.008, -0.016, 0.008, -0.008, 0.004, 0.0, 0.0, 0.0, 0.016, 0.012, -0.004, -0.012,
                -0.008, -0.008,
                -0.02, 0.0, 0.016],
               [-0.024, -0.02, 0.012, 0.012, -0.004, 0.016, 0.012, -0.036, 0.0, 0.097, 0.028, 0.004, -0.012, -0.029,
                0.008,
                -0.036, -0.012, 0.008, 0.0],
               [-0.02, 0.0, 0.008, 0.0, -0.004, -0.033, -0.024, -0.016, -0.02, 0.077, 0.028, -0.024, 0.004, 0.004,
                -0.012, 0.0,
                -0.036, 0.012, 0.016],
               [-0.016, 0.013, -0.012, 0.016, -0.012, 0.012, -0.024, -0.004, 0.0, 0.028, 0.154, -0.004, -0.024, 0.004,
                -0.004,
                -0.017, 0.02, -0.041, -0.021],
               [-0.004, 0.0, 0.004, 0.028, -0.008, -0.037, -0.016, 0.008, 0.0, -0.052, -0.037, 0.053, 0.02, -0.037,
                0.012, 0.004,
                -0.004, -0.045, -0.02],
               [-0.018, 0.004, -0.019, 0.014, 0.0, -0.016, -0.002, -0.018, 0.0, 0.0, -0.035, 0.031, -0.006, -0.014,
                -0.018,
                -0.018, -0.008, -0.018, 0.002],
               [-0.008, -0.004, 0.01, -0.026, 0.004, -0.01, 0.0, -0.004, -0.021, 0.0, -0.005, 0.016, 0.008, -0.002, 0.0,
                0.01,
                -0.008, -0.004, -0.008],
               [-0.004, -0.002, 0.006, -0.012, 0.002, -0.004, 0.0, -0.01, 0.0, 0.0, -0.027, 0.008, 0.0, -0.016, -0.004,
                0.032,
                -0.004, 0.014, -0.004],
               [0.0, 0.002, 0.008, 0.004, 0.006, -0.002, 0.004, -0.002, 0.0, 0.0, 0.014, 0.026, 0.0, 0.004, 0.002, 0.0,
                0.008,
                0.008, 0.004],
               [-0.01, 0.002, -0.006, 0.002, 0.012, 0.002, -0.008, -0.014, 0.0, 0.0, -0.045, -0.006, 0.008, 0.004,
                0.014, 0.008,
                0.006, -0.01, 0.008],
               [-0.004, -0.002, -0.008, -0.004, 0.01, -0.008, -0.008, 0.002, 0.044, 0.0, -0.027, -0.02, -0.008, 0.0,
                -0.002,
                0.002, 0.002, 0.004, -0.014],
               [0.01, 0.008, 0.008, -0.004, 0.018, -0.008, 0.008, 0.002, 0.0, 0.0, -0.018, -0.004, 0.03, -0.002, 0.004,
                0.012,
                0.01, 0.02, 0.008],
               [-0.01, -0.006, 0.004, 0.008, 0.004, 0.0, 0.002, 0.002, 0.0, 0.0, -0.043, 0.012, -0.014, 0.006, -0.006,
                -0.004,
                -0.004, 0.0, -0.018],
               [-0.002, -0.002, -0.002, -0.006, -0.008, -0.01, -0.016, -0.016, 0.0, 0.0, 0.0, -0.012, 0.016, 0.004,
                -0.002, 0.0,
                -0.012, -0.002, 0.004],
               [-0.028, 0.0, 0.016, -0.004, -0.004, 0.008, 0.0, -0.02, -0.036, 0.0, 0.0, -0.024, 0.004, -0.012, -0.016,
                -0.012,
                -0.004, 0.008, 0.012],
               [-0.036, 0.02, -0.012, 0.0, 0.008, -0.02, 0.029, 0.012, 0.0, 0.0, 0.0, -0.016, 0.025, 0.008, -0.024,
                -0.02, 0.016,
                0.028, -0.033],
               [-0.004, -0.004, -0.033, -0.021, 0.037, 0.012, 0.021, -0.012, 0.0, 0.0, 0.0, -0.02, 0.021, -0.012, 0.004,
                0.016,
                -0.037, 0.013, -0.008],
               [0.02, -0.008, -0.004, 0.012, -0.016, -0.02, 0.024, -0.028, 0.0, 0.045, 0.0, 0.008, 0.008, 0.037, 0.0,
                -0.012,
                -0.012, 0.0, -0.012],
               [0.008, 0.016, 0.016, 0.016, -0.012, -0.02, -0.012, 0.012, 0.037, 0.057, 0.0, -0.02, -0.016, 0.02,
                -0.024, -0.008,
                -0.004, -0.037, 0.008],
               [-0.012, 0.012, -0.024, 0.024, -0.02, -0.008, 0.008, -0.02, 0.0, -0.061, 0.0, 0.008, 0.0, -0.024, 0.016,
                0.016,
                -0.012, 0.02, 0.0],
               [-0.008, 0.0, 0.017, 0.029, 0.0, 0.0, -0.004, 0.049, 0.0, -0.064, 0.0, -0.004, -0.008, 0.008, 0.012,
                0.009, 0.017,
                0.004, 0.0],
               [-0.002, -0.002, -0.008, -0.004, -0.012, -0.006, -0.021, -0.014, 0.0, 0.0, 0.0, -0.021, 0.006, -0.002,
                -0.002,
                -0.012, 0.014, -0.008, 0.0],
               [0.016, 0.004, 0.0, -0.004, -0.018, 0.012, 0.014, 0.0, -0.006, 0.0, 0.0, -0.014, 0.004, -0.004, 0.014,
                -0.006,
                0.008, -0.002, 0.024],
               [0.002, -0.014, -0.012, 0.002, 0.004, 0.004, 0.004, 0.004, 0.0, 0.0, 0.0, -0.008, 0.008, 0.002, 0.0,
                0.006, 0.008,
                0.004, 0.004],
               [0.006, 0.006, -0.004, 0.002, 0.016, 0.004, 0.008, 0.006, 0.0, 0.0, 0.0, 0.004, 0.012, 0.0, 0.006, 0.006,
                0.004,
                0.014, 0.004],
               [0.004, 0.008, 0.012, 0.004, 0.0, 0.0, -0.008, 0.0, 0.0, 0.0, 0.0, 0.01, 0.008, 0.01, 0.0, 0.004, -0.004,
                0.01,
                0.002],
               [0.0, 0.0, 0.004, 0.0, 0.008, 0.002, 0.008, 0.008, 0.016, 0.0, 0.0, 0.0, 0.014, 0.002, 0.004, 0.002,
                0.016, 0.006,
                0.008],
               [0.0, 0.004, 0.004, 0.006, 0.002, 0.014, 0.004, 0.016, 0.0, 0.0, 0.0, 0.0, 0.0, 0.004, 0.01, 0.006,
                0.006, 0.004,
                0.004],
               [0.01, 0.008, 0.0, 0.0, 0.0, 0.016, 0.006, 0.012, 0.0, 0.0, 0.0, 0.004, 0.02, -0.002, 0.0, -0.002, 0.014,
                0.0,
                0.01],
               [0.012, 0.01, -0.006, -0.004, -0.004, 0.008, -0.014, -0.014, 0.0, 0.0, 0.0, -0.014, -0.018, 0.02, 0.0,
                0.0, -0.002,
                0.004, -0.01],
               [-0.028, 0.004, -0.008, -0.016, 0.004, 0.0, -0.012, -0.012, -0.024, 0.0, 0.0, -0.012, 0.004, 0.008,
                0.008, 0.02,
                -0.012, -0.008, -0.012],
               [-0.008, 0.008, 0.024, -0.004, 0.004, 0.0, 0.004, -0.004, 0.0, 0.0, 0.0, 0.0, 0.004, -0.004, 0.02, 0.008,
                -0.004,
                -0.004, 0.02],
               [0.02, -0.024, 0.024, 0.025, 0.0, 0.008, 0.041, 0.012, 0.0, 0.0, 0.0, -0.049, -0.004, -0.008, -0.017,
                -0.008,
                0.016, -0.012, -0.004],
               [-0.004, -0.008, -0.02, 0.008, -0.008, 0.024, -0.004, 0.016, 0.0, 0.121, 0.0, -0.02, -0.004, -0.02,
                -0.004, 0.004,
                -0.024, 0.004, 0.024],
               [0.004, 0.016, 0.008, -0.032, -0.004, 0.0, -0.008, -0.012, 0.162, 0.024, 0.0, 0.0, -0.036, 0.0, -0.004,
                0.004,
                -0.012, 0.012, 0.024],
               [0.016, 0.02, -0.016, -0.008, 0.008, 0.012, -0.028, -0.012, 0.0, -0.012, 0.0, -0.004, -0.016, 0.028,
                0.012, -0.008,
                -0.004, 0.012, 0.008],
               [0.028, 0.004, 0.012, -0.012, -0.021, 0.012, 0.008, 0.02, 0.0, -0.048, 0.0, -0.029, 0.004, 0.025, 0.012,
                0.012,
                0.024, 0.016, 0.017],
               [0.012, 0.006, 0.0, 0.002, -0.008, 0.027, -0.014, -0.012, 0.0, 0.0, 0.0, -0.026, -0.014, 0.022, -0.002,
                0.004,
                -0.004, 0.0, 0.01],
               [0.01, 0.014, 0.016, 0.006, -0.006, 0.008, -0.002, -0.004, 0.012, 0.0, 0.0, -0.004, 0.0, 0.002, -0.004,
                -0.01,
                -0.006, 0.012, 0.01],
               [0.0, 0.002, 0.008, 0.004, 0.008, 0.012, 0.004, 0.002, 0.0, 0.0, 0.0, -0.008, -0.006, 0.016, 0.0, -0.002,
                0.01,
                0.016, 0.01],
               [0.008, 0.006, 0.004, 0.002, 0.01, 0.008, 0.012, 0.004, 0.0, 0.0, 0.0, 0.006, -0.002, 0.008, 0.004, 0.01,
                0.01,
                0.0, 0.006],
               [0.0, -0.004, 0.004, -0.004, 0.002, -0.002, 0.004, 0.01, 0.0, 0.0, 0.0, -0.014, 0.01, 0.004, 0.0, -0.004,
                -0.01,
                0.0, -0.012],
               [0.008, 0.002, -0.018, -0.008, 0.006, -0.01, 0.004, 0.034, -0.002, 0.0, 0.0, -0.01, 0.006, -0.004, 0.004,
                -0.01,
                0.006, 0.008, -0.01],
               [0.01, 0.006, 0.008, 0.002, 0.0, 0.0, 0.004, -0.008, 0.0, 0.0, 0.0, -0.002, -0.008, -0.008, 0.008, 0.002,
                0.004,
                0.016, 0.008],
               [-0.014, -0.008, -0.004, 0.0, -0.016, -0.008, -0.006, -0.014, 0.0, 0.0, 0.0, -0.016, 0.0, 0.006, -0.002,
                0.004,
                0.004, -0.01, -0.012]]
    tspecific = [None] * (seq_length - 2)
    for j in range(seq_length - 2):
        if seq[j:j + 3] == 'AAA':
            tspecific[j] = PDNlist[0][j]
        elif seq[j:j + 3] == 'AAU':
            tspecific[j] = PDNlist[1][j]
        elif seq[j:j + 3] == 'AAC':
            tspecific[j] = PDNlist[2][j]
        elif seq[j:j + 3] == 'AAG':
            tspecific[j] = PDNlist[3][j]
        elif seq[j:j + 3] == 'AUA':
            tspecific[j] = PDNlist[4][j]
        elif seq[j:j + 3] == 'AUU':
            tspecific[j] = PDNlist[5][j]
        elif seq[j:j + 3] == 'AUC':
            tspecific[j] = PDNlist[6][j]
        elif seq[j:j + 3] == 'AUG':
            tspecific[j] = PDNlist[7][j]
        elif seq[j:j + 3] == 'ACA':
            tspecific[j] = PDNlist[8][j]
        elif seq[j:j + 3] == 'ACU':
            tspecific[j] = PDNlist[9][j]
        elif seq[j:j + 3] == 'ACC':
            tspecific[j] = PDNlist[10][j]
        elif seq[j:j + 3] == 'ACG':
            tspecific[j] = PDNlist[11][j]
        elif seq[j:j + 3] == 'AGA':
            tspecific[j] = PDNlist[12][j]
        elif seq[j:j + 3] == 'AGU':
            tspecific[j] = PDNlist[13][j]
        elif seq[j:j + 3] == 'AGC':
            tspecific[j] = PDNlist[14][j]
        elif seq[j:j + 3] == 'AGG':
            tspecific[j] = PDNlist[15][j]
        elif seq[j:j + 3] == 'UAA':
            tspecific[j] = PDNlist[16][j]
        elif seq[j:j + 3] == 'UAU':
            tspecific[j] = PDNlist[17][j]
        elif seq[j:j + 3] == 'UAC':
            tspecific[j] = PDNlist[18][j]
        elif seq[j:j + 3] == 'UAG':
            tspecific[j] = PDNlist[19][j]
        elif seq[j:j + 3] == 'UUA':
            tspecific[j] = PDNlist[20][j]
        elif seq[j:j + 3] == 'UUU':
            tspecific[j] = PDNlist[21][j]
        elif seq[j:j + 3] == 'UUC':
            tspecific[j] = PDNlist[22][j]
        elif seq[j:j + 3] == 'UUG':
            tspecific[j] = PDNlist[23][j]
        elif seq[j:j + 3] == 'UCA':
            tspecific[j] = PDNlist[24][j]
        elif seq[j:j + 3] == 'UCU':
            tspecific[j] = PDNlist[25][j]
        elif seq[j:j + 3] == 'UCC':
            tspecific[j] = PDNlist[26][j]
        elif seq[j:j + 3] == 'UCG':
            tspecific[j] = PDNlist[27][j]
        elif seq[j:j + 3] == 'UGA':
            tspecific[j] = PDNlist[28][j]
        elif seq[j:j + 3] == 'UGU':
            tspecific[j] = PDNlist[29][j]
        elif seq[j:j + 3] == 'UGC':
            tspecific[j] = PDNlist[30][j]
        elif seq[j:j + 3] == 'UGG':
            tspecific[j] = PDNlist[31][j]
        elif seq[j:j + 3] == 'CAA':
            tspecific[j] = PDNlist[32][j]
        elif seq[j:j + 3] == 'CAU':
            tspecific[j] = PDNlist[33][j]
        elif seq[j:j + 3] == 'CAC':
            tspecific[j] = PDNlist[34][j]
        elif seq[j:j + 3] == 'CAG':
            tspecific[j] = PDNlist[35][j]
        elif seq[j:j + 3] == 'CUA':
            tspecific[j] = PDNlist[36][j]
        elif seq[j:j + 3] == 'CUU':
            tspecific[j] = PDNlist[37][j]
        elif seq[j:j + 3] == 'CUC':
            tspecific[j] = PDNlist[38][j]
        elif seq[j:j + 3] == 'CUG':
            tspecific[j] = PDNlist[39][j]
        elif seq[j:j + 3] == 'CCA':
            tspecific[j] = PDNlist[40][j]
        elif seq[j:j + 3] == 'CCU':
            tspecific[j] = PDNlist[41][j]
        elif seq[j:j + 3] == 'CCC':
            tspecific[j] = PDNlist[42][j]
        elif seq[j:j + 3] == 'CCG':
            tspecific[j] = PDNlist[43][j]
        elif seq[j:j + 3] == 'CGA':
            tspecific[j] = PDNlist[44][j]
        elif seq[j:j + 3] == 'CGU':
            tspecific[j] = PDNlist[45][j]
        elif seq[j:j + 3] == 'CGC':
            tspecific[j] = PDNlist[46][j]
        elif seq[j:j + 3] == 'CGG':
            tspecific[j] = PDNlist[47][j]
        elif seq[j:j + 3] == 'GAA':
            tspecific[j] = PDNlist[48][j]
        elif seq[j:j + 3] == 'GAU':
            tspecific[j] = PDNlist[49][j]
        elif seq[j:j + 3] == 'GAC':
            tspecific[j] = PDNlist[50][j]
        elif seq[j:j + 3] == 'GAG':
            tspecific[j] = PDNlist[51][j]
        elif seq[j:j + 3] == 'GUA':
            tspecific[j] = PDNlist[52][j]
        elif seq[j:j + 3] == 'GUU':
            tspecific[j] = PDNlist[53][j]
        elif seq[j:j + 3] == 'GUC':
            tspecific[j] = PDNlist[54][j]
        elif seq[j:j + 3] == 'GUG':
            tspecific[j] = PDNlist[55][j]
        elif seq[j:j + 3] == 'GCA':
            tspecific[j] = PDNlist[56][j]
        elif seq[j:j + 3] == 'GCU':
            tspecific[j] = PDNlist[57][j]
        elif seq[j:j + 3] == 'GCC':
            tspecific[j] = PDNlist[58][j]
        elif seq[j:j + 3] == 'GCG':
            tspecific[j] = PDNlist[59][j]
        elif seq[j:j + 3] == 'GGA':
            tspecific[j] = PDNlist[60][j]
        elif seq[j:j + 3] == 'GGU':
            tspecific[j] = PDNlist[61][j]
        elif seq[j:j + 3] == 'GGC':
            tspecific[j] = PDNlist[62][j]
        elif seq[j:j + 3] == 'GGG':
            tspecific[j] = PDNlist[63][j]
    return tspecific


def ncp(seq):
    seq_length = len(seq)
    ncp_lsit = [None] * seq_length * 3
    for j in range(seq_length):
        if seq[j] == 'A':
            ncp_lsit[j * 3] = 1
            ncp_lsit[j * 3 + 1] = 1
            ncp_lsit[j * 3 + 2] = 1
        elif seq[j] == 'U':
            ncp_lsit[j * 3] = 0
            ncp_lsit[j * 3 + 1] = 0
            ncp_lsit[j * 3 + 2] = 1
        elif seq[j] == 'C':
            ncp_lsit[j * 3] = 0
            ncp_lsit[j * 3 + 1] = 1
            ncp_lsit[j * 3 + 2] = 0
        elif seq[j] == 'G':
            ncp_lsit[j * 3] = 1
            ncp_lsit[j * 3 + 1] = 0
            ncp_lsit[j * 3 + 2] = 0
    return ncp_lsit


def nd(seq):
    seq_length = len(seq)
    nd_list = [None] * seq_length
    for j in range(seq_length):
        if seq[j] == 'A':
            nd_list[j] = round(seq[0:j].count('A') / (j + 1), 3)
        elif seq[j] == 'U':
            nd_list[j] = round(seq[0:j].count('U') / (j + 1), 3)
        elif seq[j] == 'C':
            nd_list[j] = round(seq[0:j].count('C') / (j + 1), 3)
        elif seq[j] == 'G':
            nd_list[j] = round(seq[0:j].count('G') / (j + 1), 3)
    return nd_list


with open(file_input) as f:
    data = f.readlines()
list1 = data[1::2]
list1 = [k.strip() for k in list1]
names = data[0::2]
names = [k[1:].strip() for k in names]
sample_length = len(names)  # sample_number    seq_length
newlist = [None] * sample_length
sequence = []
for k in range(sample_length):
    newlist[k] = names[k] + ' ' + list1[k]
for line in newlist:
    label = ''
    if 'P' in line:
        label = '+1'
        sequence = line.split(' ')
    elif 'N' in line:
        label = '-1'
        sequence = line.split(' ')
    else:
        print('error')
        break
    print(label, *psnp(sequence[1]), *dnc(sequence[1]), file=file_out)
file_out.close()

# print(label, *nc(sequence[1]), *dnc(sequence[1]), *tnc(sequence[1]), *psnp(sequence[1]), *psdp(sequence[1]),
#       *pstp(sequence[1]), *ncp(sequence[1]), *nd(sequence[1]), file=file_out)
