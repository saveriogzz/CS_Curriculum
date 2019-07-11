#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:24:34 2019

@author: saveriogzz
"""

def remainingBalance1(balance, annualInterestRate, monthlyPaymentRate):
    
    i = 12
    
    while i > 0:
        
        minPayment = balance*monthlyPaymentRate
        ub = balance - minPayment
        interest = (annualInterestRate/12)*ub
        
        balance = ub + interest
        i -= 1
        
    return print('Remaining balance: {}'.format(round(balance, 2)))


def remainingBalance2(balance, annualInterestRate, monthlyPaymentRate):
    balance *= ((1 - monthlyPaymentRate) * (1 + annualInterestRate/12))**12
    return round(balance, 2)