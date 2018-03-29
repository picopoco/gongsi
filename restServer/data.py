#!/usr/bin/env python
# -*- coding: utf-8 -*-
lmsBody = {
	"transactionId": "aaadafadf3",
	"messageId": "test001",
	"deviceToken": "32c51b9fa79f45b88b08393422046fee",
	"customerId": "ljw76@naver.com",
	"contentType": "",
	"contentLen": "",
	"common": {
		"resultCode": "COIF20000000",
		"resultMsg": "성공(정상처리) ",
		"resultCodeTrace": "20000000"
	},
	"body": {
		"utterByContents": "samsung lepeat.",
		"utterByContentsEnc": "",
		"skillName": "lms",
		"intentName": "lmsRepeatPlay",
		"currentPosition": "",
		"slotInfo": {
			"messageType": "NORMAL",
			"data": ""
		},
		"lmsContents": {
			"paidProductYn": "Y",
			"lectureId": "0000000001",
			"lectureName": "samsung education app",
			"chapterId": "1",
			"chapterName": "",
			"sampleYn": "N",
			'data': {}
		},
		"userInfo": {
			"loginYn": "Y",
			"chapterIdYn": "N"
		}
	}
}

lmsData = {'1k1c_c':
				[ {
				    'menuId':'1k1c1c',
					'repeatSeq': '1',
					'TeacherText': ['I am going to'],
					'answerText': 'I am going to',
					'answerPoint': '25,25,25,25',
					'keyWordPosition': '-1',
					'repeatName': '1k1c1c',
					'repeatUrl': '1k1c1c.mp3',
					'hint': '',
					'picture': ''
				},
				  {
					'menuId': '1k1c2c',
					'repeatSeq': '2',
					'TeacherText': ['she is going to'],
					'answerText': 'she is going to',
					'answerPoint': '25,25,25,25',
					'keyWordPosition': '-1',
					'repeatName': '1k1c2c',
					'repeatUrl': '1k1c2c.mp3',
					'hint': '',
					'picture': ''

				},
					{
					'menuId': '1k1c3c',
					'repeatSeq': '3',
					'TeacherText': ['They are going to'],
					'answerText': 'They are going to',
					'answerPoint': '25,25,25,25',
					'keyWordPosition': '-1',
					'repeatName': '1k1c3c',
					'repeatUrl': '1k1c3c.mp3',
					'hint': '',
					'picture': ''
				},
				 {
					'menuId': '1k1c4c',
					'repeatSeq': '4',
					'TeacherText': ['go shopping'],
					'answerText': 'go shopping',
					'answerPoint': '50,50',
					'keyWordPosition': '-1',
					'repeatName': '1k1c4c',
					'repeatUrl': '1k1c4c.mp3',
					'hint': '',
					'picture': ''
				}],
				#1cunk warm
			  '1k1c_w': [
					{
					'menuId': '1k1c1w',
					'repeatSeq': '5',
					'TeacherText': ['난~하려고'],
					'answerText': 'I am going to',
					'answerPoint': '25,25,25,25',
					'keyWordPosition': '-1',
					'repeatName': '1k1c1w',
					'repeatUrl': '1k1c1w.mp3',
					'hint': '',
					'picture': ''
				},
					{'1k1c2w' : {
					'menuId': '1k1c2w',
					'repeatSeq': '6',
					'TeacherText': ['그녀는~할거야'],
					'answerText': 'she is going to',
					'answerPoint': '25,25,25,25',
					'keyWordPosition': '-1',
					'repeatName': '1k1c2w',
					'repeatUrl': '1k1c2w.mp3',
					'hint': '',
					'picture': ''
				}},
					{'1k1c3w' : {
					'menuId': '1k1c3w',
					'repeatSeq': '7',
					'TeacherText': ['그들은~할 거야'],
					'answerText': 'They are going to',
					'answerPoint': '25,25,25,25',
					'keyWordPosition': '-1',
					'repeatName': '1k1c3w',
					'repeatUrl': '1k1c3w.mp3',
					'hint': '',
					'picture': ''
				}},
					{'1k1c4w' : {
					'menuId': '1k1c4w',
					'repeatSeq': '8',
					'TeacherText': ['쇼핑 가'],
					'answerText': 'go shopping',
					'answerPoint': '50,50',
					'keyWordPosition': '-1',
					'repeatName': '1k1c4w',
					'repeatUrl': '1k1c4w.mp3',
					'hint': '',
					'picture': ''
				}}
					],
			# 1cunk sentence
			  '1k1c_s':	[
      			  {
					'menuId': '1k1c1s',
					'repeatSeq': '9',
					'TeacherText': ['난 쇼핑가려고'],
					'answerText': 'I am going to go shopping',
					'answerPoint': '15,10,15,15,15,15,15',
					'keyWordPosition': '-1',
					'repeatName': '1k1c1s',
					'repeatUrl': '1k1c1s.mp3',
					'hint': '',
					'picture': ''
		    	},
					 {
					'menuId': '1k1c2s',
					'repeatSeq': '10',
					'TeacherText': ['걔들은 쇼핑갈 거야'],
					'answerText': 'they are going to go shopping',
					'answerPoint': '15,15,15,15,15,25',
					'keyWordPosition': '-1',
					'repeatName': '1k1c2s',
					'repeatUrl': '1k1c2s.mp3',
					'hint': '',
					'picture': ''
					},
					{
					'menuId': '1k1c3s',
					'repeatSeq': '11',
					'TeacherText': ['그녀는 쇼핑갈 거야'],
					'answerText': 'she is going to go shopping',
					'answerPoint': '15,15,15,15,15,25',
					'keyWordPosition': '-1',
					'repeatName': '1k1c3s',
					'repeatUrl': '1k1c3s.mp3',
					'hint': '',
					'picture': ''
					}],
		########## 2chunk 1clue ###########
              '1k2c_c':	[
				     {
						'menuId': '1k1c1c',
						'repeatSeq': '1',
						'TeacherText': ['tomorrow'],
						'answerText': 'tomorrow',
						'answerPoint': '100',
						'keyWordPosition': '-1',
						'repeatName': '1k2c1c',
						'repeatUrl': '1k2c1c.mp3',
						'hint': '',
						'picture': ''
					},
					{'1k2c2c' : {
						    'menuId': '1k1c1c',
						    'repeatSeq': '2',
							'TeacherText': ['go to the shopping mall'],
							'answerText': 'go to the shopping mall',
							'answerPoint': '20,20,20,20,20',
							'keyWordPosition': '-1',
							'repeatName': '1k2c2c',
							'repeatUrl': '1k2c2c.mp3',
							'hint': '',
							'picture': ''
					}},
					{'1k2c3c' : {
							'menuId': '1k2c3c',
							'repeatSeq': '3',
							'TeacherText': ['with my friends'],
							'answerText': 'with my friends',
							'answerPoint': '30,30,40',
							'keyWordPosition': '-1',
							'repeatName': '1k2c3c',
							'repeatUrl': '1k2c3c.mp3',
							'hint': '',
							'picture': ''
					}},
					{'1k2c4c' : {
							'menuId': '1k1c1c',
							'repeatSeq': '4',
							'TeacherText': ['I want to'],
							'answerText': 'I want to',
							'answerPoint': '25,50,25',
							'keyWordPosition': '-1',
							'repeatName': '1k2c4c',
							'repeatUrl': '1k2c4c.mp3',
							'hint': '',
							'picture': ''
					}},
					{'1k2c5c' : {
							'menuId': '1k1c1c',
							'repeatSeq': '5',
							'TeacherText': ['today'],
							'answerText': 'today',
							'answerPoint': '100',
							'keyWordPosition': '-1',
							'repeatName': '1k2c5c',
							'repeatUrl': '1k2c5c.mp3',
							'hint': '',
							'picture': ''
					}}],

		      # 2cunk warm
			  '1k2c_w':[
					{'1k2c1w' : {
						'menuId': '1k1c1c',
						'repeatSeq': '5',
						'TeacherText': ['쇼핑몰에 가'],
						'answerText': 'go to shopping mall',
						'answerPoint': '25,25,25,25',
						'keyWordPosition': '-1',
						'repeatName': '1k2c1w',
						'repeatUrl': '1k2c1w.mp3',
						'hint': '',
						'picture': ''
					}},
			         {'1k2c2w' : {
						'menuId': '1k1c1c',
						'repeatSeq': '6',
						'TeacherText': ['내 친구들이랑'],
						'answerText': 'with my friends',
						'answerPoint': '30,30,40',
						'keyWordPosition': '-1',
						'repeatName': '1k2c2w',
						'repeatUrl': '1k2c2w.mp3',
						'hint': '',
						'picture': ''
					}},
					{'1k2c3w' : {
						'menuId': '1k1c1c',
						'repeatSeq': '7',
						'TeacherText': ['난 ~하고 싶어'],
						'answerText': 'I want to',
						'answerPoint': '30,30,40',
						'keyWordPosition': '-1',
						'repeatName': '1k2c3w',
						'repeatUrl': '1k2c3w.mp3',
						'hint': '',
						'picture': ''
					}}],

			  # 1cunk sentence
			  '1k2c_s': [
					{'1k2c1s' : {
						'menuId': '1k1c1c',
						'repeatSeq': '8',
						'TeacherText': ['난 내일 쇼핑몰에 가고 싶어'],
						'answerText': 'I want to go to shopping mall tomorrow',
						'answerPoint': '10,10,10,10,10,20,10,20',
						'keyWordPosition': '-1',
						'repeatName': '1k2c1s',
						'repeatUrl': '1k2c1s.mp3',
						'hint': '',
						'picture': ''
					}},
					{'1k2c2s' : {
						'repeatSeq': '9',
						'menuId': '1k1c1c',
						'TeacherText': ['난 오늘 쇼핑몰에 가고 싶어'],
						'answerText': 'I want to go to shopping mall today',
						'answerPoint': '10,10,10,10,10,20,10,20',
						'keyWordPosition': '-1',
						'repeatName': '1k2c2s',
						'repeatUrl': '1k2c2s.mp3',
						'hint': '',
						'picture': ''
					}},
					{'1k2c3s' : {
						'repeatSeq': '10',
						'menuId': '1k1c1c',
						'TeacherText': ['난 내 친구들이랑 쇼핑몰에 가고 싶어'],
						'answerText': 'I want to go to shopping mall with my friends',
						'answerPoint': '10,10,10,10,10,10,10,10,10,10',
						'keyWordPosition': '-1',
						'repeatName': '1k2c3s',
						'repeatUrl': '1k2c3s.mp3',
						'hint': '',
						'picture': ''
					}}],

		####1 kang expression clue
			  '1k1e1c':[
				  {'1k1e1c' : {
					  'menuId': '1k1c1c',
					  'repeatSeq': '1',
						'TeacherText': ['that is awesome'],
						'answerText': 'that is awesome',
						'answerPoint': '30,30,40',
						'keyWordPosition': '-1',
						'repeatName': '1k1e1c',
						'repeatUrl': '1k1e1c.mp3',
						'hint': '',
						'picture': ''
					},
				  '1k1e2c' : {
						'repeatSeq': '2',
					    'menuId': '1k1c1c',
					    'TeacherText': ['that is awesome'],
						'answerText': 'that is awesome',
						'answerPoint': '30,30,40',
						'keyWordPosition': '-1',
						'repeatName': '1k2c2c',
						'repeatUrl': '1k2c.mp3',
						'hint': '',
						'picture': ''
				  },
			      '1k1e3c' : {
					'menuId': '1k1c1c',
					'repeatSeq': '3',
					'TeacherText': ['that is awesome'],
					'answerText': 'that is awesome',
					'answerPoint': '30,30,40',
					'keyWordPosition': '-1',
					'repeatName': '1k1e3c',
					'repeatUrl': '1k1e3c.mp3',
					'hint': '',
					'picture': ''
				  }}],

		#####1 lecture expression warm
			  '1k1e_w':[
				 {'1k1e1w' : {
					'menuId': '1k1c1c',
					'repeatSeq': '2',
					'TeacherText': ['멋지다!'],
					'answerText': 'that is awesome',
					'answerPoint': '30,30,40',
					'keyWordPosition': '-1',
					'repeatName': '1k1e1w',
					'repeatUrl': '1k1e1w.mp3',
					'hint': '',
					'picture': ''
			  },
				  '1k1e2w' : {
					  	    'menuId': '1k1c1c',
					 	    'repeatSeq': '3',
							'TeacherText': ['끝내주는데?'],
							'answerText': 'that is awesome',
							'answerPoint': '30,30,40',
							'keyWordPosition': '-1',
							'repeatName': '1k1s3c',
							'repeatUrl': '1k1s3c.mp3',
							'hint': '',
							'picture': ''
					 },
				  '1k1e3w' : {
						    'menuId': '1k1c1c',
						    'repeatSeq': '3',
							'TeacherText': ['완전 좋아!'],
							'answerText': 'that is awesome',
							'answerPoint': '30,30,40',
							'keyWordPosition': '-1',
							'repeatName': '1k1e3w',
							'repeatUrl': '1k1e3w.mp3',
							'hint': '',
							'picture': ''
						}}],
			#speaking
			  '1k1e_s':[
				 {'1k1e1s' : {
				 'menuId': '1k1c1c',
				 'repeatSeq': '3',
				'TeacherText': ['야~ 나 공짜 영화 티켓이 생겼어.','Hey, I got free movi tickets.','완전 좋은데?'],
				'answerText': 'that is awesome',
				'answerPoint': '30,30,40',
				'keyWordPosition': '-1',
				'repeatName': '1k1e1s',
				'repeatUrl': '1k1e1s.mp3',
				'hint':'',
				'picture': '1k1e1s.jpg'
			
		}}],

		# Talk conversation
		      '1k1t_o':[
				  {'1k1t1o' : {
					'repeatSeq': '3',
					'TeacherText': ['너 뭐하고 싶어?','what do you want to do?','난 내 친구들이랑 쇼핑몰에 가고 싶어'],
					'answerText': 'I want to go to the shopping mall with my friends',
					'answerPoint': '5,10,5,10,10,10,10,10,10,10,10',
					'keyWordPosition': '-1',
					'repeatName': '1k1t1o',
					'repeatUrl': '1k1t1o.mp3',
					'hint': '',
					'picture': ''
				},
				'1k1t2o' : {
					'repeatSeq': '3',
					'TeacherText': ['이건 내 새 자전거야!','this is my new bike!', '우와 멋지다'],
					'answerText': 'that is awesome',
					'answerPoint': '30,30,40',
					'keyWordPosition': '-1',
					'repeatName': '1k1t2o',
					'repeatUrl': '1k1t2o.mp3',
					'hint': '',
					'picture': ''
				},
				'1k1t3o' : {
					'repeatSeq': '3',
					'TeacherText': ['너 무슨 계획있어?','do you have any plans?', 'I am going to'],
					'answerText': 'I am going to',
					'answerPoint': '20,20,40,20',
					'keyWordPosition': '-1',
					'repeatName': '1k1t3o',
					'repeatUrl': '1k1t3o.mp3',
					'hint': '',
					'picture': ''
				}}],
}

def lmslepeatSample(menuCode):
	res = {}
	if menuCode in lmsData:
		res = lmsData[menuCode]
	lmsBody['body']['lmsContents']['repeat'] = res
	return lmsBody


def getlmsRepeatData(dataList):
	lmsBody['body']['lmsContents']['repeat'] = dataList
	return lmsBody

def lmsRepeatCurrentPosition():
 data = {
            "common": {
                "method": " lmsRepeatCurrentPosition",
                "resultCode": "COIF20000000",
                "resultCodeTrace": "MSSX20000000|COIF20000000",
                "resultMessage": "성공",
                "schema": " outSpeech"
            }
 }

 def lmsRepeaterror():
	 data =	 {
		 "transactionId": '',
		 "messageId": '',
		 "deviceToken": '',
		 "customerId": '',
		 "contentType": '',
		 "contentLen": '',
		 "common": {
			 "schema": "Audio",
			 "method": "play",
			 "resultCode": "COIF25140002",
			 "resultMsg": "슬럿정보가 없습니다.",
			 "resultCodeTrace": "COIF25140002"
		 },
		 "body": {
			 "utterByContents": '',
			 "utterByContentsEnc": '',
			 "skillName": '',
			 "intentName": '',
			 "slotInfo": {
				 "messageType": '',
				 "data": ''
			 },
			 "ucfc": {
				 "shouldEndSession": True,
				 "outputSpeech": []
			 },
			 "directiveId": '',
			 "directiveBody": {
				 "serviceName": '',
				 "playBehavior": '',
				 "progressReportInterval": '',
				 "playIndex": '',
				 "playListCount": '',
				 "playList": []
			 },
			 "deviceControl": {
				 "beep": '',
				 "led": ''
			 }
		 }
	 }
 return data

def lmsRepeatCurrentPosition():
	data = {
		'common': {
			'method': ' lmsRepeatCurrentPosition',
			'resultCode': 'COIF20000000',
			'resultCodeTrace': 'MSSX20000000|COIF20000000',
			'resultMessage': '성공',
			'schema': ' outSpeech'
		}
	}

	def lmsRepeaterror():
		data =	 {
			'transactionId': '',
			'messageId': '',
			'deviceToken': '',
			'customerId': '',
			'contentType': '',
			'contentLen': '',
			'common': {
				'schema': 'Audio',
				'method': 'play'
				,
				'resultCode': 'COIF25140002',
				'resultMsg': '슬럿정보가 없습니다.',
				'resultCodeTrace': 'COIF25140002'
			},
			'body': {
				'utterByContents': '',
				'utterByContentsEnc': '',
				'skillName': '',
				'intentName': '',
				'slotInfo': {
					'messageType': '',
					'data': ''
				},
				'ucfc': {
					'shouldEndSession': True,
					'outputSpeech': []
				},
				'directiveId': '',
				'directiveBody': {
					'serviceName': '',
					'playBehavior': '',
					'progressReportInterval': '',
					'playIndex': '',
					'playListCount': '',
					'playList': []
				},
				'deviceControl': {
					'beep': '',
					'led': ''
				}
			}
		}
	return data

if __name__ == '__main__':
     print lmslepeatSample('1k1c1c')


