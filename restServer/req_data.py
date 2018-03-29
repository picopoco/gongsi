#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Head(transactionId='', customerId='', deviceToken=''):
	head = {
		"Content-Type": "application/json;charset=UTF-8",
	}
	return head

def RequestlmsPlayData(moveType='',  chapter=''):

	if chapter:
		chaptName = 'chapter'

	data = {
	"common" : {
		"serviceType" : "SVC_003",
		"deviceLanguage" : "ko_KR",
		"triggerType":"KDB",
		"logData" : {
			"clientIp" : "192.168.0.100",
			"devInfo" : "PHONE",
			"osInfo" : "android_7.0.0",
			"nwInfo" : "5G",
			"devModel" : "LE-E250",
			"svcName":"INWF",
			"svcType":"SVC_003",
			"devType" : "DEV_009",
			"carrierType":"L"
		}
	},
	"body" : {
		"skill" : "lms",
		"intent" : "lmsRepeatPlay",
		"slot" : {
			"lecture" : "samsung english",
			"moveType":moveType,
			"lvl1": {"name": chaptName, "value": chapter},
				}
	}
}
	return data

