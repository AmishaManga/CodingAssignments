%% 
%Name: Amisha Manga
%Date: 20/01/2022
%Code: The code below plots the raw radar data provided, and plots the micro
%doppler spectrum of the shuriken in an attempt to identify
%which suspect attacked 'Garmin'

%%
close all;
fclose all;
clear all;
clc;
format compact;
format short;

addpath('Functions');

%% Read IF Data from CSV file
rawData = csvread('RadarData.csv');

%% Plot Raw Data in Time Domain
figure;
plot(rawData);
title("Received IF Signal in Time Domain");

%% Plot Raw Data in Frequency Domain
figure;
fftRawData = fft(rawData); % Zero pad to 16384, next power of 2
%fftRawData = fft(rawData, 2^14, 2); % Zero pad to 16384, next power of 2
plot(20*log10(abs(fftRawData)));
title("Received IF Signal in Frequency Domain");

%% Params for Spectrogram Function

WinL =128;                          % fft window length
overLap = 8;                        % overlap size
nfft = 1024;                        % zero padding for window fft
beta = 2.5;                         % shape factor for kaiser filter: sdie lobe attenuation
dbdown = 20;                        % limiting the range of STFT values to the maximum value

%% Draw Spectrogram
STFTM = Specgram(rawData,WinL , overLap, nfft, beta);
STFTM = 20*log10(abs(STFTM));

% Find maximum value in the db plot
STFTMdbmax = max(STFTM(:)); 
caxis = [STFTMdbmax-dbdown STFTMdbmax]; 

figure;
SpecAxis = imagesc(STFTM, caxis);
ylabel('Frequency (kHz)'); 
xlabel('Time (ms)'); 
title('Micro-Doppler Spectrum of Mystery Shuriken');
colorbar;
colormap(jet);

% Label Axes
yticklabels = -5:1:5;     % 10 kHz
xticklabels = 0:100:1000; % 1 second
set(gca, 'YTick', linspace(1, nfft, numel(yticklabels)), 'YTickLabel', flipud(yticklabels(:)), ...
'XTick',linspace(1, width(STFTM), numel(xticklabels)), 'XTickLabel', xticklabels );
