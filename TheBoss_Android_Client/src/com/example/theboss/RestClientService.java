package com.example.theboss;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;

public class RestClientService extends Service {

	@Override
	public IBinder onBind(Intent arg0) {
		// TODO Auto-generated method stub
		return null;
	}
	 @Override
	 public void onStart(Intent intent, int startId) {
		 
	 // Toast.makeText(this, "Service start", Toast.LENGTH_SHORT).show();
	  //if (m!=null) m.stop();
	  //m = MediaPlayer.create(this, R.raw.deal); //raw是放mp3的資料夾,deal是mp3的檔名
	  //m.start();
	 }
	 

}
