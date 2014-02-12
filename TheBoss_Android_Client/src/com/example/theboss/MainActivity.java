package com.example.theboss;

import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.view.*;
import android.widget.ImageView;
import android.graphics.Bitmap;
import android.widget.Button;

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

class RestHandler extends Thread {

	String TARGET_URL = "";
	String RESULT = "";

	public void setTargetURL(String url) {
		this.TARGET_URL = url;
	}

	public void run() {
		this.RESULT = getTicketFromURL();

	}

	private String convertStreamToString(java.io.InputStream is) {
		java.util.Scanner s = new java.util.Scanner(is).useDelimiter("\\A");
		return s.hasNext() ? s.next() : "";
	}

	private String getTicketFromURL() {
		System.out.println("get result?!");
		String result = "";
		URL url;
		HttpURLConnection urlConnection;
		JSONObject json;
		try {
			url = new URL(TARGET_URL);
			urlConnection = (HttpURLConnection) url.openConnection();

			urlConnection.setRequestMethod("PUT");
			InputStream in = new BufferedInputStream(
					urlConnection.getInputStream());
			json = new JSONObject(convertStreamToString(in));
			result = json.getString("sid");
			System.out.println("get result?!");
		} catch (Exception e) {
			e.printStackTrace();
		} finally {

		}
		return result;
	}

}

public class MainActivity extends Activity {

	ImageView qrView;
	private static String GET_TICKET_URL = "http://118.161.24.136:5000/Service/test1/Person";
	RestHandler restHandler = new RestHandler();

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		final Button btGenerateQr = (Button) findViewById(R.id.btGenerateQr);
		final Button btDoWebApi = (Button) findViewById(R.id.btDoWebApi);
		qrView = (ImageView) findViewById(R.id.qrCode);
		btGenerateQr.setOnClickListener(new View.OnClickListener() {
			public void onClick(View v) {
				System.out.println("to generate QR");
				// Perform action on click
				background.start();

			}

			Thread background = new Thread(new Thread() {

	

				// After call for background.start this run method call
				public void run() {

					String result = "";
					URL url;
					HttpURLConnection urlConnection;
					JSONObject json;
					try {
						url = new URL(GET_TICKET_URL);
						
						urlConnection = (HttpURLConnection) url
								.openConnection();

						urlConnection.setRequestMethod("PUT");
						InputStream in = new BufferedInputStream(urlConnection
								.getInputStream());
						json = new JSONObject(convertStreamToString(in));
						result = json.getString("sid");
						System.out.println("get result?!" + result);
						generateQr(result);
					} catch (Exception e) {
						e.printStackTrace();
					} finally {

					}

				}

				private String convertStreamToString(java.io.InputStream is) {
					java.util.Scanner s = new java.util.Scanner(is)
							.useDelimiter("\\A");
					return s.hasNext() ? s.next() : "";
				}

			});
			
			

		});
		btDoWebApi.setOnClickListener(new View.OnClickListener() {
			public void onClick(View v) {
				doWebApi();
				// Perform action on click
				System.out.println("to generate QR");
				Log.e("aa", "msg");
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
