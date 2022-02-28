%% https://www.mathworks.com/matlabcentral/answers/104488-spectrogram-plot-without-using-spectrogram-command

function [STFTM] = Specgram(y,WinL,overlap, nfft, beta)
%%
% y : Input Signal
% WinL: window Length in no. of samples
% overlap : overlap in no. of samples
% nfft: Number of DFT points for FFT
% beta: shape factor for kaiser filter: side lobe attenuation
%%
    L = length(y); % Length of input signal
    STFT = [];
    
    if (overlap == 0)
        frameCount = floor(L/WinL);
    else 
        nFr = round(L/overlap); %no. of frames
        frameCount = nFr  - round(WinL/overlap);
    end
    
    for i = 1: frameCount % count of frames 
        FB = (i-1)*overlap+1; % Beginning Frame 
        FE = FB + WinL -1; %Frame End 
        fftSeg = y(FB:FE);
        winVec = kaiser(length(fftSeg), beta)'; % beta value
        %winVec = Hann(length(fftSeg))';
        winVec = winVec / sum(winVec);
        STFT(:,i) = fftshift(fft(fftSeg.*winVec, nfft));
        %STFT(:,i) = fft(fftSeg, nfft);
    end
    STFTM = STFT; 
end