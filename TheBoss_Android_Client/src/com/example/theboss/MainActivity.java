package com.example.theboss;

import android.os.AsyncTask;
import android.os.Bundle;
import android.app.Activity;
import android.content.Context;
import android.util.Log;
import android.view.*;
import android.widget.ImageView;
import android.graphics.Bitmap;
import android.widget.Button;
import android.widget.TextView;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;

import java.io.BufferedInputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Random;
import java.lang.Runnable;

import org.json.JSONObject;

class RestClientTask extends AsyncTask<String, Void, String> {
	Context contextGUI;
	  public RestClientTask(Context callerclass)
	    {
	        contextGUI = callerclass;
	    }
	  
  
    protected String doInBackground(String... urls) {
    	RestExecutor restExecutor = new RestExecutor(urls[0],"PUT");
    	JSONObject result = restExecutor.run();
        return result.toString();
        
    }
    
    protected void onPostExecute(String result) {
    	TextView myTextView = (TextView) ((MainActivity) contextGUI).findViewById(R.id.textView2);
    	myTextView.setText(result);
    	
    }
}

public class MainActivity extends Activity implements ThreadCallBack{

	ImageView qrView;
	private static String GET_TICKET_URL = "http://118.165.192.32:8080/Service/rest1/Person";
	RestAsynExecutor REST_CLIENT ;
	ThreadCallBack CALL_BACK;
    TextView myTextView ;
    MainActivity SELF_REF;
	public void callback(){
		JSONObject result = this.REST_CLIENT.getResult();
		System.out.println(result);
		setContentView(R.layout.activity_main);
	        myTextView = (TextView)findViewById(R.id.textView2);
	        myTextView.setText(result.toString());
	}
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		this.CALL_BACK = this;
		setContentView(R.layout.activity_main);
		final Button btGenerateQr = (Button) findViewById(R.id.btGenerateQr);
		final Button btDoWebApi = (Button) findViewById(R.id.btDoWebApi);
		qrView = (ImageView) findViewById(R.id.qrCode);
		SELF_REF = this;
		btGenerateQr.setOnClickListener(new View.OnClickListener() {
			public void onClick(View v) {
				System.out.println("to generate QR");
				// Perform action on click
				new RestClientTask(SELF_REF).execute(GET_TICKET_URL);
		
			}
		});
		
	}

	private String convertStreamToString(java.io.InputStream is) {
		java.util.Scanner s = new java.util.Scanner(is).useDelimiter("\\A");
		return s.hasNext() ? s.next() : "";
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);

		return true;
	}

	public static void doWebApi() {

	}

	public static String genRandomString() {
		Random generator = new Random();
		String x = new Integer((generator.nextInt(96) + 32)).toString();
		return x;
	}

	public void generateQr(String qrData) {
		int qrCodeDimention = 500;

		QRCodeEncoder qrCodeEncoder = new QRCodeEncoder(qrData, null,
				Contents.Type.TEXT, BarcodeFormat.QR_CODE.toString(),
				qrCodeDimention);

		try {
			Bitmap bitmap = qrCodeEncoder.encodeAsBitmap();
			qrView.setImageBitmap(bitmap);
		} catch (WriterException e) {
			e.printStackTrace();
		}

	}

}
